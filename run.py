import polars as pl
from polars_tor import is_tor_node, is_tor_exit_node

# Example DataFrame with IP addresses
df = pl.DataFrame({
    "ip_addresses": ["1.1.1.1", "185.220.101.1", "8.8.8.8"]
})

# Load the Tor nodes list
tor_nodes_path = "tor-nodes.csv"

# Perform the lookup for Tor nodes
df = df.with_columns(
    is_tor_node(df["ip_addresses"]).alias("is_tor_node")
)

# Load the Tor exit nodes list
tor_exit_nodes_path = "tor-exit-nodes.csv"

# Perform the lookup for Tor exit nodes
df = df.with_columns(
    is_tor_exit_node(df["ip_addresses"]).alias("is_tor_exit_node")
)

print(df)