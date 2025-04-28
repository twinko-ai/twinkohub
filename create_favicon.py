from PIL import Image

# Open the logo image
logo_path = 'themes/twinkohub/static/images/logo.png'
favicon_path = 'themes/twinkohub/static/images/favicon.ico'

# Open the logo
with Image.open(logo_path) as img:
    # Create a new image with transparent background
    favicon = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    
    # Calculate the size to fit the logo in the favicon
    # while maintaining aspect ratio
    ratio = min(32/img.width, 32/img.height)
    new_size = (int(img.width * ratio), int(img.height * ratio))
    
    # Resize the logo
    resized = img.resize(new_size, Image.Resampling.LANCZOS)
    
    # Calculate position to center the logo
    position = ((32 - new_size[0]) // 2, (32 - new_size[1]) // 2)
    
    # Paste the resized logo onto the transparent background
    favicon.paste(resized, position)
    
    # Save as favicon.ico
    favicon.save(favicon_path, format='ICO', sizes=[(32, 32)])

print(f"Favicon created at: {favicon_path}") 