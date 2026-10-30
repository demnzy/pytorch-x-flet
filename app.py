import flet as ft
import torch
import os
from train_model import AirQualityModel
# ==========================================
# Session 3: Bringing it Together
# Goal: Build a Flet UI for our PyTorch Model
# ==========================================

# 1. Initialize and load our trained PyTorch model
model = AirQualityModel()
try:
    # Resolve the absolute path of the model relative to this script
    model_path = os.path.join(os.path.dirname(__file__), 'model.pth')
    model.load_state_dict(torch.load(model_path, weights_only=True))
    model.eval() # Set model to evaluation mode
    model_loaded = True
except FileNotFoundError:
    model_loaded = False
    print("Warning: model.pth not found. Please run train_model.py first.")

def predict_aqi(temperature, humidity, pm25):
    """Helper function to run our PyTorch model and get a prediction"""
    if not model_loaded:
        return "Model not loaded!"
    
    # Convert inputs to a PyTorch tensor
    input_tensor = torch.tensor([[temperature, humidity, pm25]], dtype=torch.float32)
    
    # Run the model without tracking gradients
    with torch.no_grad():
        prediction = model(input_tensor)
        
    return prediction.item()

def main(page: ft.Page):
    # Setup Page
    page.title = "AI Air Quality Predictor"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0 # Full bleed background
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Use a modern font
    page.fonts = {
        "Inter": "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bslnt%2Cwght%5D.ttf"
    }
    page.theme = ft.Theme(font_family="Inter")
    
    # UI Elements
    dashboard_result = ft.Text("0.0", size=60, weight=ft.FontWeight.W_900, color=ft.Colors.WHITE)
    aqi_label = ft.Text("Predicted AQI", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE70)

    # Interactive Sliders
    temp_slider = ft.Slider(min=10, max=40, value=25, label="{value} °C", active_color=ft.Colors.ORANGE_400)
    humidity_slider = ft.Slider(min=20, max=90, value=50, label="{value} %", active_color=ft.Colors.BLUE_400)
    pm25_slider = ft.Slider(min=0, max=200, value=20, label="{value} µg/m³", active_color=ft.Colors.RED_400)

    def update_prediction(e):
        """Runs the PyTorch model instantly when a slider is moved!"""
        aqi = predict_aqi(temp_slider.value, humidity_slider.value, pm25_slider.value)
        if isinstance(aqi, str):
            dashboard_result.value = aqi
        else:
            dashboard_result.value = f"{aqi:.1f}"
            
            # Dynamic color coding based on AQI severity
            if aqi < 50:
                dashboard_result.color = ft.Colors.GREEN_400
            elif aqi < 100:
                dashboard_result.color = ft.Colors.YELLOW_400
            elif aqi < 150:
                dashboard_result.color = ft.Colors.ORANGE_400
            else:
                dashboard_result.color = ft.Colors.RED_400
                
        page.update()

    # Link the sliders to the AI function
    temp_slider.on_change = update_prediction
    humidity_slider.on_change = update_prediction
    pm25_slider.on_change = update_prediction
    
    # Run a prediction instantly on startup
    if model_loaded:
        update_prediction(None)
    
    # ----------------------------------------
    # Building the Premium Glassmorphic UI
    # ----------------------------------------
    
    main_card = ft.Container(
        content=ft.Column(
            controls=[
                # Header
                ft.Row([
                    ft.Icon(ft.Icons.AIR, color=ft.Colors.WHITE, size=35), 
                    ft.Text("AI Environment Monitor", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER),
                
                ft.Divider(color=ft.Colors.WHITE24, height=40),
                
                # The AQI Display Box
                ft.Container(
                    content=ft.Column([aqi_label, dashboard_result], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                    alignment=ft.Alignment.CENTER,
                    padding=ft.Padding.all(25),
                    border_radius=ft.BorderRadius.all(20),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE)
                ),
                
                ft.Divider(color=ft.Colors.TRANSPARENT, height=20), # Spacer
                
                # The Controls
                ft.Text("Temperature", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_400),
                temp_slider,
                
                ft.Text("Humidity", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_400),
                humidity_slider,
                
                ft.Text("PM2.5 Level", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_400),
                pm25_slider,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        ),
        width=480,
        padding=ft.Padding.all(40),
        border_radius=ft.BorderRadius.all(30),
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
        blur=ft.Blur(15, 15)
    )
    
    # The Background Canvas
    background = ft.Container(
        content=main_card,
        expand=True,
        alignment=ft.Alignment.CENTER,
        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
            colors=[ft.Colors.BLUE_900, ft.Colors.PURPLE_900]
        ),
        padding=ft.Padding.all(20)
    )

    page.add(background)

if __name__ == "__main__":
    ft.run(main)
