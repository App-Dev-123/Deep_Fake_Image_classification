import streamlit as st

# Define a dictionary to map each combination of selections to its corresponding image filenames
import os

image_dir = "C:/Users/sahit/dl_images/"

image_mapping = {
    ("AlexNet", "Base model"): [os.path.join(image_dir, "alexNet_base_model_1.png"), os.path.join(image_dir, "alexNet_base_model_2.png")],
    ("AlexNet", "L2 regularization"): [os.path.join(image_dir, "alexnet_l2_reg_1.png"), os.path.join(image_dir, "alexnet_l2_reg_2.png")],
    ("AlexNet", "early stopping"): [os.path.join(image_dir, "alexnet_early_stopping_1.png"), os.path.join(image_dir, "alexnet_early_stopping_2.png")],
    ("VGG", "Base model"): [os.path.join(image_dir, "vgg_base_model_1.png"), os.path.join(image_dir, "vgg_base_model_2.png")],
    ("VGG", "L2 regularization"): [os.path.join(image_dir, "vgg_l2_reg_1.png"), os.path.join(image_dir, "vgg_l2_reg_2.png")],
    ("VGG", "early stopping"): [os.path.join(image_dir, "vgg_l2_reg_1.png"), os.path.join(image_dir, "vgg_l2_reg_2.png")],
    ("XceptionNet", "Base model"): [os.path.join(image_dir, "xception_base_model_1.png"), os.path.join(image_dir, "xception_base_model_2.png")],
    ("XceptionNet", "L2 regularization"): [os.path.join(image_dir, "xception_l2_reg_1.png"), os.path.join(image_dir, "xception_l2_reg_2.png")],
    ("XceptionNet", "early stopping"): [os.path.join(image_dir, "xception_early_stopping_1.png"), os.path.join(image_dir, "xception_early_stopping_2.png")],
    ("AlexNet + RNN", "Base model"): [os.path.join(image_dir, "alexnet_rnn_base_model_1.jpg"), os.path.join(image_dir, "alexnet_rnn_base_model_2.jpg")],
    ("AlexNet + RNN", "L2 regularization"): [os.path.join(image_dir, "alexnet_rnn_l2_reg_1.jpg"), os.path.join(image_dir, "alexnet_rnn_l2_reg_2.jpg")],
    ("AlexNet + RNN", "early stopping"): [os.path.join(image_dir, "alexnet_rnn_early_stopping_1.jpg"), os.path.join(image_dir, "alexnet_rnn_early_stopping_2.jpg")],
    ("Vision Transformer", "Base model"): [os.path.join(image_dir, "vit_base_model_1.jpg"), os.path.join(image_dir, "vit_base_model_2.png")],
    ("Vision Transformer", "L2 regularization"): [os.path.join(image_dir, "vit_base_model_1.jpg"), os.path.join(image_dir, "vit_base_model_2.png")],
    ("Vision Transformer", "early stopping"): [os.path.join(image_dir, "vit_early_stopping_1.jpg"), os.path.join(image_dir, "vit_early_stopping_2.jpg")],
    ("Ensemble Method (DenseNet, ALexnet, ResNet -18,ViT)", "Base model"): [os.path.join(image_dir, "ensemble_base_model_1.jpg"), os.path.join(image_dir, "ensemble_base_model_2.jpg")],
    ("Ensemble Method (DenseNet, ALexnet, ResNet -18,ViT)", "L2 regularization"): [os.path.join(image_dir, "ensemble_l2_reg_1.jpg"), os.path.join(image_dir, "ensemble_l2_reg_2.jpg")],
    ("Ensemble Method (DenseNet, ALexnet, ResNet -18,ViT)", "early stopping"): [os.path.join(image_dir, "ensemble_early_stopping_1.jpg"), os.path.join(image_dir, "ensemble_early_stopping_2.jpg")],
}

# Function to display images based on dropdown selections
def display_images(selected_option_1, selected_option_2):
    st.write(f"Selected Option 1: {selected_option_1}")
    st.write(f"Selected Option 2: {selected_option_2}")
    
    # Get the image filenames based on the selections
    images = image_mapping.get((selected_option_1, selected_option_2))
    
    # Display the images if available
    if images:
        st.image(images[0], caption="Image 1", use_column_width=True)
        st.image(images[1], caption="Image 2", use_column_width=True)
    else:
        st.write("No images available for the selected combination.")

# Main function to create the Streamlit page
def admin_page():
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
    st.title("Results")
    st.write("Please select options from the dropdowns")

    # Dropdown menus to select options
    selected_option_1 = st.selectbox("Select Option 1", ["AlexNet", "VGG", "XceptionNet", "AlexNet + RNN", "Vision Transformer", "Ensemble Method (DenseNet, ALexnet, ResNet -18,ViT)"], index=None)
    selected_option_2 = st.selectbox("Select Option 2", ["Base model", "L2 regularization", "early stopping"], index=None)

    # Display images based on the selected options
    display_images(selected_option_1, selected_option_2)

# Run the main function
if __name__ == "__main__":
    admin_page()
