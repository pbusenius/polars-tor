# Polars Tor-Node-Lookup Plugin

This plugin extends the functionality of [Polars](https://www.pola.rs) by providing a method to check whether IP addresses are known Tor nodes or Tor exit nodes. The result is returned as a boolean value (True/False).

## Features

- **Tor Node Lookup:** Checks if the provided IP addresses are included in a list of known Tor nodes or Tor exit nodes.
- **Integration with Polars:** Works seamlessly with Polars DataFrames, offering fast processing.

## Requirements

- Python 3.8+
- Polars library

Install Polars with:

```bash
uv add polars
```

- Tor Node List: The list of Tor nodes must be provided as a file (e.g., `tor-nodes.csv`) in CSV format. This file can be downloaded from sources such as the [dan.me](https://www.dan.me.uk/torlist) or other maintained Tor node lists.

- Tor Exit Node List: The list of Tor exit nodes must be provided as a file (e.g., `tor-exit-nodes.csv`) in CSV format.

## Installation

Add the plugin to your project. Install it directly from the repository or manually include the Python file.

```bash
uv add polars-tor
```

## Usage

### Example Code

```python
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
```

### Output

If `tor-nodes.csv` contains `185.220.101.1` and `tor-exit-nodes.csv` does not, the output will look like this:

```
shape: (3, 3)
┌───────────────────┬──────────────┬───────────────────┐
│ ip_addresses      │ is_tor_node  │ is_tor_exit_node  │
├───────────────────┼──────────────┼───────────────────┤
│ 1.1.1.1           │ false        │ false             │
│ 185.220.101.1     │ true         │ false             │
│ 8.8.8.8           │ false        │ false             │
└───────────────────┴──────────────┴───────────────────┘
```