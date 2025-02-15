# Standard library
import glob
import os
import subprocess
import sys
import time
# Third party
import streamlit as st

st.set_page_config(layout="wide")  # <>
st.title("Demonstration of accessing Github repository")  # <>
left, right = st.columns(2)  # Split the main page in two columns

# LEFT SIDE with the public repository
left.header("Use a public repository")
try:
    from public_repository import code as public_code
    public_code.make_dataframe(left)
    public_code.make_graph(left)
except ImportError as ie:
    left.write(f"could not import public_repository : {ie}")

# RIGHT SIDE with the private repository
right.header("Use a private repository")
token = os.environ.get("token")
if token:
    st.toast(f"Token was found: {len(token)}")
right.write(os.listdir())
# get current directory
path = os.getcwd()
right.write(f"Current Directory: {path}")
search_path = os.path.join(*[".."]*3, "**", "*.zip")
paths = glob.glob(search_path, recursive=True)
# parent directory
parent = os.path.dirname(path)
right.write(f"Parent directory {parent}")
right.write(paths)
result = subprocess.Popen(
    [(f'{sys.executable}'
        " -m pip install "
        f'git+https://{token}@github.com/UnicornOnAzur/closed_repository.git')
     ],
    shell=True)
# wait for subprocess to install package before running your actual code below
time.sleep(30)
right.write(os.listdir())
time.sleep(30)
right.write(os.listdir())
try:
    from private_repository import code as private_code
    private_code.make_dataframe(right)
    private_code.make_graph(right)
except ImportError as ie:
    right.write(f"could not import private_repositoy : {ie}")
