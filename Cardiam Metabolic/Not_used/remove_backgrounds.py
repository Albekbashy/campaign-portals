from PIL import Image
import os

# Directory with JPG files
logo_dir = r"c:\Users\abdul\Downloads\Project_HTML_SHO8L - Copy\Mind_Communication_Interface.2\Mind_Communication_Interface\Cardiam Metabolic"

jpg_files = [
    "globalpharma logo_page-0001.jpg",
    "CMbrix logo p_page-0001.jpg",
    "Atorlip logo_page-0001.jpg",
    "Emiros logo_page-0001.jpg",
    "Glovadip logo_page-0001.jpg",
    "Emijan M logo_page-0001.jpg",
    "Ruset logo _page-0001.jpg",
    "Sartan logo_page-0001.jpg"
]

for jpg_file in jpg_files:
    jpg_path = os.path.join(logo_dir, jpg_file)
    
    if os.path.exists(jpg_path):
        # Open image
        img = Image.open(jpg_path).convert('RGBA')
        
        # Get image data
        data = img.getdata()
        new_data = []
        
        # Replace white/light background with transparency
        for item in data:
            # If pixel is white or very light (RGB > 240), make it transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(item)
        
        img.putdata(new_data)
        
        # Save as PNG with transparency
        png_file = jpg_file.replace('.jpg', '.png')
        png_path = os.path.join(logo_dir, png_file)
        img.save(png_path, 'PNG')
        print(f"✓ Converted: {jpg_file} → {png_file}")

print("\n✅ All logos processed! Backgrounds removed and converted to PNG.")
