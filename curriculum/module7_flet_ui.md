# Day 2/3 - Module 7: Building Modern UIs with Flet

Our AI brain is trapped inside a `.pth` file. It's smart, but completely useless to a normal human being who doesn't know how to code. We need to build a User Interface (UI) so people can interact with it.

---
## Day 2 Content (30 mins)

### 1. What is Flet? (10 mins)

Flet is a magical framework that allows you to build beautiful, modern, interactive apps for Windows, Mac, Linux, iOS, Android, and the Web... entirely in Python! Behind the scenes, Flet uses Google's "Flutter" engine to draw the graphics.

### 2. Flet Fundamentals & Layouts (20 mins)

Every Flet app revolves around the `Page`. Think of the `Page` as your blank canvas.
You add **Controls** (UI elements) to the canvas. Flet has dozens of controls: `ft.Text`, `ft.Button`, `ft.Slider`, etc.

If you just throw controls onto a page, it looks messy. We use layouts to organize them:
- **`ft.Row`**: Arranges items horizontally side-by-side.
- **`ft.Column`**: Arranges items vertically stacked on top of each other.
- **`ft.Container`**: A box that you can wrap around a control to give it padding, borders, background colors, and gradients!

```python
import flet as ft

def main(page: ft.Page):
    # Notice we use a Python List [] to hold the controls!
    my_column = ft.Column(controls=[
        ft.Text("Hello World!"),
        ft.ElevatedButton(text="Click Me")
    ])
    page.add(my_column)

ft.run(main) # Starts the app!
```

---
## Day 3 Content (60 mins)

### 3. Modern Aesthetics & Glassmorphism (30 mins)

We don't just want a UI; we want a *beautiful* UI. We can use Flet's `ft.Container` to create modern effects like "Glassmorphism" (making UI elements look like frosted glass).

To do this, we use properties like:
- `bgcolor=ft.colors.with_opacity(0.1, ft.colors.WHITE)`
- `border_radius=ft.BorderRadius.all(30)`
- `blur=ft.Blur(15, 15)`

Notice that Flet properties like `ft.colors`, `ft.padding`, and `ft.margin` are written in **lowercase**, while the specific enums inside them (like `ft.Padding.all()`) use standard casing!

### 4. Interactivity (The Domino Effect) (30 mins)

A beautiful slider is useless if it doesn't do anything. We need to connect our UI to Python functions.
We do this using **Event Handlers**, specifically `on_change` for our sliders.

Look closely at this line of code:
`temp_slider.on_change = update_prediction`

Notice that `update_prediction` does **not** have parentheses `()` after it. 
- If we wrote `update_prediction()`, the computer would run the function *immediately* while building the UI.
- By omitting the parentheses, we are handing the slider a map to the recipe and saying: *"Hold onto this. When a human drags you, follow the map and run the recipe!"*

Inside that function, you can read the values of your sliders, update the text on the screen, and force the UI to refresh by calling `page.update()`. This creates a seamless, interactive experience where the AI predicts live as you drag!
