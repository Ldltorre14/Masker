import customtkinter as ctk
import cv2
import numpy as np
from PIL import Image, ImageOps
from io import BytesIO
import requests

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Masker")
        self.geometry("1080x720")
        self.resizable(False, False)
        self.config(bg="black")
        
        self.cap = cv2.VideoCapture(0)
        
        self.renderGUI()
        
        # Schedule the first frame update
        self.updateFrame()
    
    def renderGUI(self):
        self.titleLabel = ctk.CTkLabel(master=self, text="Masker", corner_radius=10, 
                                       fg_color="#39ff14", bg_color="black",
                                       font=("Comic Sans MS", 40))
        
        self.ogFilterLabel = ctk.CTkLabel(master=self, text="Original", corner_radius=10, 
                                          text_color="#39ff14", bg_color="black",
                                          font=("Comic Sans MS", 28))
        
        self.filteredLabel = ctk.CTkLabel(master=self, text="Filter", corner_radius=10, 
                                          text_color="#39ff14", bg_color="black",
                                          font=("Comic Sans MS", 28))
        
        self.optionList = ctk.CTkComboBox(master=self, 
                                          values=["Original", "Black&White", "Negative", "Rotate 90°", 
                                                  "Rotate 180°", "Rotate 270°", "Canny"],
                                          text_color="#39ff14", bg_color="black",
                                          corner_radius=10, button_color="#39ff14",
                                          fg_color="black", border_color="#39ff14", 
                                          dropdown_fg_color="#39ff14")
        
        self.videoLabel = ctk.CTkLabel(master=self)
        self.filteredVideoLabel = ctk.CTkLabel(master=self)  # New label for filtered image
        
        self.titleLabel.place(x=440, y=50)
        self.ogFilterLabel.place(x=160, y=200)
        self.filteredLabel.place(x=800, y=200)
        self.optionList.place(x=800, y=650)
        self.videoLabel.place(x=160, y=250)  # Adjust the position as needed
        self.filteredVideoLabel.place(x=500, y=250)  # Adjust the position as needed
        
        # Bind the option list to call applyFilterAndUpdate when an option is selected
        self.optionList.bind("<<ComboboxSelected>>", self.applyFilterAndUpdate)
        
    def updateFrame(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert frame to JPEG format for transmission
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = BytesIO(buffer)
        
            # Display original image
            img = Image.open(frame_bytes)
            img = ImageOps.exif_transpose(img)  # Fix orientation issues
            img = img.resize((400, 300))  # Resize the image
            ctk_img = ctk.CTkImage(light_image=img, size=(img.width, img.height))
            self.videoLabel.configure(image=ctk_img)
            self.videoLabel.image = ctk_img
    
        # Apply filter to the image
        selected_filter = self.optionList.get()
        processed_image_bytes = self.applyFilter(frame_bytes, selected_filter)
    
        if processed_image_bytes:
            # Display processed image
            img = Image.open(BytesIO(processed_image_bytes))
            img = ImageOps.exif_transpose(img)  # Fix orientation issues
            img = img.resize((400, 300))  # Resize the image
            ctk_img = ctk.CTkImage(light_image=img, size=(img.width, img.height))
            self.filteredVideoLabel.configure(image=ctk_img)  # Update the filtered image label
            self.filteredVideoLabel.image = ctk_img

        # Schedule the next frame update
        self.after(10, self.updateFrame)
    
    def applyFilterAndUpdate(self, event):
        selected_filter = self.optionList.get()
        print(selected_filter)
        
        # Convert current frame to JPEG format for transmission
        _, buffer = cv2.imencode('.jpg', self.cap.read()[1])
        frame_bytes = BytesIO(buffer)
        
        # Apply filter to the image
        processed_image_bytes = self.applyFilter(frame_bytes, selected_filter)
        
        if processed_image_bytes:
            # Display processed image
            img = Image.open(BytesIO(processed_image_bytes))
            img = ImageOps.exif_transpose(img)  # Fix orientation issues
            ctk_img = ctk.CTkImage(light_image=img, size=(img.width, img.height))
            self.filteredVideoLabel.configure(image=ctk_img)  # Update the filtered image label
            self.filteredVideoLabel.image = ctk_img
    
    def applyFilter(self, frame_bytes, selected_filter):
        # Define the API endpoint
        api_url = "http://localhost:5000/process_image"  # Replace with your API URL

        # Prepare the data for the POST request
        data = {'filter': selected_filter}
        files = {'image': frame_bytes.getvalue()}

        # Make the POST request
        response = requests.post(api_url, data=data, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the processed image bytes
            return response.content
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None

    def run(self):
        self.mainloop()