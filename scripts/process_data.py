import os
import pandas as pd
import networkx as nx
import numpy as np

# Paths for raw and processed data files
raw_data_dir = "../data/raw"          # Ruta ajustada según indicación
processed_data_dir = "../data/processed"
os.makedirs(processed_data_dir, exist_ok=True)

# Raw data files
airports_file = os.path.join(raw_data_dir, "airports.dat")
routes_file = os.path.join(raw_data_dir, "routes.dat")

def clean_and_process():
    # # Load airports data
    airports = pd.read_csv(
        airports_file,
        header=None,
        sep=',',
        quotechar='"',
        skipinitialspace=True,
        names=['id', 'name', 'city', 'country', 'IATA', 'ICAO', 
            'lat', 'lon', 'alt', 'tz', 'dst', 'tz_db', 'type', 'source']
    )

    # Convert 'id' to numeric, coercing errors to NaN
    airports['id'] = pd.to_numeric(airports['id'], errors='coerce')
    # Drop rows with invalid 'id'
    airports = airports.dropna(subset=['id'])
    # Convert 'id' to int
    airports['id'] = airports['id'].astype(int)

    # Load routes data
    routes = pd.read_csv(
        routes_file,
        header=None,
        sep=',',
        quotechar='"',
        skipinitialspace=True,
        names=['airline', 'airline_id', 'src_airport', 'src_id', 
               'dst_airport', 'dst_id', 'codeshare', 'stops', 'equipment']
    )
    
    # Convert 'src_id' and 'dst_id' to numeric, coercing errors to NaN
    routes['src_id'] = pd.to_numeric(routes['src_id'], errors='coerce')
    routes['dst_id'] = pd.to_numeric(routes['dst_id'], errors='coerce')
    # Drop rows with invalid 'src_id' or 'dst_id'
    routes_clean = routes.dropna(subset=['src_id', 'dst_id'])
    # Convert to int
    routes_clean.loc[:, 'src_id'] = routes_clean['src_id'].astype(int)
    routes_clean.loc[:, 'dst_id'] = routes_clean['dst_id'].astype(int)


    # Remove self-loops
    routes_clean = routes_clean[routes_clean['src_id'] != routes_clean['dst_id']]
    
    # Create graph
    G = nx.Graph()
    # Add nodes (airports)
    for _, row in airports.iterrows():
        G.add_node(int(row['id']), 
                   name=row['name'], city=row['city'], country=row['country'],
                   IATA=row['IATA'], ICAO=row['ICAO'], lat=row['lat'], lon=row['lon'])
    # Add edges (routes)
    edges = list(zip(routes_clean['src_id'], routes_clean['dst_id']))
    G.add_edges_from(edges)
    
    # Extract the giant component
    largest_cc = max(nx.connected_components(G), key=len)
    Gc = G.subgraph(largest_cc).copy()
    
    # Print network info
    print(f"Total nodes: {G.number_of_nodes()}")
    print(f"Total edges: {G.number_of_edges()}")
    print(f"Number of connected components: {nx.number_connected_components(G)}")
    print(f"Largest connected component: {Gc.number_of_nodes()} nodes, {Gc.number_of_edges()} edges")
    
    # Save in HDF5 format
    nodes_df = pd.DataFrame.from_dict(dict(Gc.nodes(data=True)), orient='index')

    nodes_df.index.name = 'id'
    nodes_df.to_hdf(os.path.join(processed_data_dir, "airports_processed.h5"), key='nodes', mode='w')
    
    edges_df = pd.DataFrame(list(Gc.edges()), columns=['src_id', 'dst_id'])
    edges_df.to_hdf(os.path.join(processed_data_dir, "routes_processed.h5"), key='edges', mode='w')
    
    print("Data processed and saved in HDF5 format.")

if __name__ == "__main__":
    clean_and_process()
