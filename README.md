# ATLAS Open Data Contributions

Welcome to the **ATLAS Open Data Contributions app**! This Streamlit-based application allows users to explore, filter, and view contributions to the ATLAS Open Data project. All project data is loaded from a projects.json file, making it easy to update or add new entries.

## How to Add Entries

To add a new entry to the project database, edit the `projects.json` file. Each entry should follow this format:
```json
{
    "name": "Project Gamma",
    "responsible": "Carol",
    "email": "email@email.com",
    "language": "language",
    "difficulty": "easy",
    "link": "https://example.com/gamma",
    "tags": ["NLP", "Machine Learning"],
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQGw4KMJCqwe9ov7cXcqOTz0BstASoGM_uug&s"
}
```

## Image Guidelines

- **Online Images**: Use a direct URL in the image field.
- **Local Images**: Place the image file in the image folder of the repository and reference it in the image field using a relative path (e.g., `./image/your_image.png`).

## Folder Structure

```
.
├── Dockerfile            # Dockerfile for the app
├── LICENSE               # Apache 2.0 License
├── README.md             # This readme file
├── app.py                # Main Streamlit application
├── projects.json         # JSON file containing project data
├── requirements.txt
├── image/                # Folder for storing local images (not created yet, feel free to do so!)
│   ├── your_image.png    # Example local image
```

## Development Notes

### Prerequisites

Ensure the following are installed:

- Python 3.7+
- Streamlit
- Pandas

### Running the App

1. Clone the repository.

2. Install dependencies using:

```pip install -r requirements.txt```

3. Run the app:

```streamlit run app.py```

4. Access the app in your browser at http://localhost:8501.

## Contribution Guidelines

We welcome contributions to this project! Follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes (e.g., update projects.json or improve the app).
4. Submit a pull request.

## License
This project is licensed under the Apache 2.0 License. See the LICENSE file for details.
