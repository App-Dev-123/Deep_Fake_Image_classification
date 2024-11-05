import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import transforms
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import alexnet, resnet18, densenet121
import timm
from timm.data.transforms_factory import create_transform

def user():
    st.set_page_config(
        page_title="Deep Learning",
        layout="wide",
    )
    def transform_image(uploaded_image):
    # Open the image
        image = Image.open(uploaded_image)
        data_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize((224, 224)),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                std=[0.229, 0.224, 0.225])
        ])
        
        # Apply the transformation
        transformed_img = data_transform(image)
        transformed_img = transformed_img.unsqueeze(0)
    
        return transformed_img
    def classify_image(model, transformed_image, threshold=0.5):
    # Pass the transformed image through the mode
        model.eval()
        
        outputs = model(transformed_image)
        
        # Apply softmax to get probabilities
        probabilities = F.sigmoid(outputs)
        # Extract probability for class 1
        probability_class_1 = probabilities[:, 1].item()
        
        # Classify as 0 or 1 based on the threshold
        predicted_label = 1 if probability_class_1 > threshold else 0

        return predicted_label
    
    st.markdown(
        """
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            div.block-container {
                padding-top: 0 !important;
                padding-right: 0 !important;
                padding-left: 0 !important;
                }
            .st-emotion-cache-18ni7ap{
                display: none !important;
                padding:0 !important;
                }
            .navbar {
                background-color: #333;
            }
    
            .navbar a {
                color: #f2f2f2;
            }
    
            .navbar a:hover {
                background-color: #ddd;
                color: black;
            }
    
            .navbar a.active {
                background-color: #04AA6D;
                color: white;
            }
            .signout-btn {
                position: absolute;
                top: 8px;
                right: 8px;
                color: white;
                cursor: pointer;
                justify-content:center;
                align-items:center;
            }
            .logo{
                max-height: 10px;
                width: auto;
                height: auto;
                padding-top:0;
                align-items:center;
                }
        </style>
        <script>
            function signOut() {
                Streamlit.setComponentValue(true, "signout");
            }
        </script>
        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class='logo'><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYQEN-P488zA8PbdEj3yS4nJSieq2jXDO2pUAX8KHOVke6LhASFKuuHHbekV1Sbjiqa9k&usqp=CAU" width="100" /></div>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">Home</a>
                    </li>
                </ul>
            </div>
            <div class="signout-btn" onclick="signOut()"><a class="nav-link" href="http://localhost:8501/#"">Sign Out</a></div>

        </nav>
        """,
        unsafe_allow_html=True,
    )

        #file upload
    center_file_uploader_style = """
        <style>
            div[data-testid="stFileUploader"] {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 200vh;
            }
            .upload-btn, .read-btn, .analysis-btn{
                display: inline-block;
                padding: 10px 5px;
                background-color: #4CAF50;
                color: white;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                cursor: pointer;
                justify-content:center;
                align-items:center;
                border-radius: 8px;
                }
            .st-emotion-cache-900wwq{
                display:flex
                flex-direction: row;
                justify-content:center;
                align-items:center;
                padding-top: 30px;
                }
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
        }
    
        </style>
    """
    st.markdown(center_file_uploader_style, unsafe_allow_html=True)
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    col1, col0,col2, col3 = st.columns([2,2,2,2])

    with col2:
        upload_button = st.button("Upload", key = "upload-btn",help="Click to upload the file")
    if upload_button:
        transformed_image = transform_image(uploaded_image)
        class Ensemble(nn.Module):
            def __init__(self, num_classes):
                super(Ensemble, self).__init__()
                
                # Load pre-trained models
                self.alexnet = alexnet(pretrained=True)
                self.vit = timm.create_model("vit_base_patch16_224", pretrained=True)
                self.densenet = densenet121(pretrained=True)
                self.resnet = resnet18(pretrained=True)
                
                # Modify the classifiers to match the number of output classes
                self.alexnet.classifier[6] = nn.Linear(4096, num_classes)
                self.vit.head = nn.Linear(self.vit.head.in_features, num_classes)
                self.densenet.classifier = nn.Linear(1024, num_classes)
                self.resnet.fc = nn.Linear(512, num_classes)
                
                # Enable gradient calculation for the last layer
                self.alexnet.classifier[6].requires_grad_(True)
                self.vit.head.requires_grad_(True)
                self.densenet.classifier.requires_grad_(True)
                self.resnet.fc.requires_grad_(True)
                
            def forward(self, x):
                # Forward pass through each model
                alexnet_out = self.alexnet(x.clone())  # Clone input to avoid in-place modification
                vit_out = self.vit(x.clone())
                densenet_out = self.densenet(x.clone())
                resnet_out = self.resnet(x)
                
                # Average the predictions from each model
                avg_out = (alexnet_out + vit_out + resnet_out + densenet_out) / 4
                
                return avg_out

        # Example usage:
        num_classes = 2  # Change this to the number of output classes in your dataset
        model = Ensemble(num_classes)
        with open('dl.pth', 'rb') as file:
            model.load_state_dict(torch.load('dl.pth', map_location=torch.device('cpu')))
        predicted_label= classify_image(model, transformed_image)
        st.markdown(
            """
            <style>
            .center {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                text-align: center;
                height: 20vh;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<h1 style='text-align: center;'>Classification Result:</h1>", unsafe_allow_html=True)

        if predicted_label == 1:
            st.markdown("<div class='center'><h2>Image is real</h2></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='center'><h2>Image is Fake</h2></div>", unsafe_allow_html=True)


        #
if __name__ == "__main__":
    user()
