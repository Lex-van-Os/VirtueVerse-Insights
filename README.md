# VirtueVerse-Insights

Python API with machine learning for processing user insights through machine learning for the project VirtueVerse

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Pip (Python package manager) installed.

### Installation

1. Create a virtual environment (recommended) to manage your project's dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Launch the API

1. Start the Flask development server with automatic code reloading (for development):

   ```bash
   flask run --reload
   ```

   Your API will be accessible at `http://localhost:5000`.

2. For production or when deploying the API to a web server, use a production-ready server like Gunicorn or uWSGI:

   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 your_app:app
   ```

   Replace `your_app` with the name of your Flask app instance.

### Usage

The VirtueVerse insights API is to be used together with the VirtueVerse project. Although requests to this API can be made seperately, it is recommended to use requests through VirtueVerse, to have a correct input and response of data.

---
