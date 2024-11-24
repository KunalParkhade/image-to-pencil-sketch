## **Image to Pencil Sketch Transformer 🖌️✨**

A **Streamlit-based web application** that converts images into stunning pencil sketches, powered by cutting-edge Firebase integration for user authentication and image storage.

---

## 🖼️ **Screenshots**

### 📂 Home Page

![Home Page](assets/Home%20page.png)

### 🖼️ Image to Pencil Sketch Example

![Example](assets/Pencil%20sketch%20example.png)

---

## 🎯 **Features**

- 🔒 **User Authentication**: Secure signup and login with Firebase.
- 📂 **Cloud Storage**: Store and retrieve images seamlessly via Firebase.
- 🖼️ **Pencil Sketch Conversion**: Transform any image into an artistic pencil sketch.
- 🎨 **Interactive UI**: User-friendly interface built with Streamlit.
- 🚀 **Deployment-Ready**: Designed for hosting on Streamlit Cloud.

---

## 🚀 **Technologies Used**

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Firebase Admin SDK
- **Programming Language**: Python
- **Libraries**:
  - `opencv-python`: Image processing
  - `firebase-admin`: Firebase integration
  - `streamlit`: UI and app management

---

## 📂 **Directory Structure**

```plaintext
image-to-pencil-sketch/
├── app/
│   ├── __init__.py            # For modular programming
│   ├── auth.py                # Handles user authentication
│   ├── firebase_config.py     # Firebase initialization
│   ├── main.py                # Main Streamlit app
│   ├── utils.py               # For common functionalities
├── requirements.txt           # Python dependencies
├── firebase_credentials.json  # Firebase service account key (hidden in .gitignore)
├── .gitignore
├── .streamlit/
│   └── secrets.toml           # Secrets for deployment (hidden in .gitignore)
└── README.md                  # Project documentation

```

## 🛠️ **Installation**

Follow these steps to set up the project locally:<br>
1️⃣ **Clone the Repository**

```bash
git clone https://github.com/KunalParkhade/image-to-pencil-sketch.git
cd image-to-pencil-sketch
```

2️⃣ **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

> If having conda: (can use different python versions also)

```bash
conda create -p venv python==3.8 -y
```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ Set Up Firebase

- Place your Firebase credentials JSON file in the root directory.
- Update `.streamlit/secrets.toml` with (prefer putting these into secrets tab while deploying using streamlit):

```toml
[firebase_credentials]
type = "service_account"
project_id = "your_project_id"
private_key_id = "your_private_key_id"
private_key = "your_private_key"
client_email = "your_client_email"
client_id = "your_client_id"
```

---

## 🏃 **Run the Application**

Launch the app locally with:

```bash
streamlit run app/main.py
```

---

## 🌐 **Deployment on Streamlit Cloud**

1. Push the code to a GitHub repository.
2. Add `secrets.toml` data to Streamlit Cloud Secrets.
3. Deploy directly from your repository.

---

## 📸 **Usage**

1. **Sign Up / Log In**: Use Firebase authentication to create or access your account.
2. **Upload Image**: Select an image to transform into a pencil sketch.
3. **Download Sketch**: Save the resulting sketch to your device.

---

## 🧪 **Developer Notes**

### 🔑 **Environment Variables**

Keep sensitive data like Firebase credentials secure using `.gitignore` and Streamlit secrets.

### 🐛 **Debugging Tips**

- Use `streamlit secrets` to access Firebase credentials during deployment.
- Check logs in Streamlit Cloud for deployment errors.

### 🎉 Enhancement Ideas

- Add support for color sketches.
- Enable social sharing of sketches directly from the app.

---

## 📜 **License**

This project is licensed under the MIT License.

---

## 🤝 Contribute

Contributions are always welcome! To get started:

1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.

---

## 🛠️ **Acknowledgements**

- [Streamlit](https://streamlit.io/)
- [Firebase](https://firebase.google.com/)
- [OpenCV](https://opencv.org)

---

## 💬 **Feedback**

Value your feedback! Reach out via:

- Email: kunalparkhade@gmail.com
- GitHub Issues: [Open an Issue](https://github.com/KunalParkhade/image-to-pencil-sketch/issues)

---

### 🙌 **Happy Coding!**
