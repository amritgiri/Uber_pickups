# Uber_pickups
Uber pickup data visualization using streamlit library python

## Installation

Open a terminal and run:

```bash
$ pip install streamlit
$ streamlit hello
```

If this opens our sweet _Streamlit Hello_ app in your browser, you're all set! If not, head over to [ docs](https://docs.streamlit.io/library/get-started) for specific installs.


## Quickstart

### A little example

Create a new file `streamlit_app.py` with the following code:
```python
import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```

Now run it to open the app!
```
$ streamlit run streamlit_app.py
```