from taipy.gui import Gui
# Define the content of the page with an iframe
page_content = """
# Advertisement Panel

<iframe src="https://thecodes.tech/backend-img/" width="100%" height="500"></iframe>
"""

# Create a Gui instance and run the application
gui = Gui(page=page_content)
gui.run()
