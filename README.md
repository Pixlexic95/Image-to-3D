# Real Image-to-3D Mesh Generation
This portfolio demonstrates how real unprocessed image data from an underwater marine environment was segmented and then generated into a 3D mesh using MeshyAI. Producing an accessible, low cost pipeline for high fidelity VR simulations.

<table align="center">
  <tr>
    <td align="center"><img src="https://github.com/user-attachments/assets/2fd7b3a6-0657-466b-a141-b1bf0598f178" /></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/88f334d6-d1a6-43db-9679-52256cbbe0d3" /></td>
  </tr>
  <tr>
    <td align="center">3D Generated Mesh of Scuba Diver Toy</td>
    <td align="center">3D Generated Mesh of Blue Box</td>
  </tr>
</table>

## Key Outputs
1. Amph3D Dataset
2. Sim-to-Real Benchmark and Augmentation
3. Conservation VR Prototype

## Project Goal
Realistic virtual reality simulations should be a pre-deployment safety check for all AUVs/ROVs. My goal here is to ensure that marine debris clearing using automation is always safety checked for conservation purposes, the marine ecoysystem is extremely fragile, so when we target automated cleanups, the AUV should collect/remove only the items that it is confident is anthropogenic waste. Part of ensuring realism in this environment requires assets that accurately represent the marine debiris - so the 3D dataset has been generated from real world image segments.<br> If it collects or disturbs part of the marine habitat in any way, it has failed. 

### Current Status
Whilst the experiments have been completed, the 3D dataset is in the process of being uploaded to Figshare and a research publication is being written. 

### Project Architecture
The Amph3D Dataset was created using the following workflow:

```
Amphitrite v1 Segments (SAM)
  ↓
  Quality check
    ↓
    Meshy.AI (API)
    ├── 3D Mesh Generation
    └── Texture Map Generation
      ↓
      Quality Assurance
        ↓
        Amph3D Dataset
```
The remaining project follows two Tracks, as described below:<br>

#### Track A: Sim-to-Real Benchmark and Augmentation
```
Amph3D Dataset
  ↓
  Blender Cycles Rendering
    └── Multi-View Data Augmentation
```
The 3D assets were rendered from multiple angles to test as a potential option for augmentation of a dataset. Read more about the experiment and results in my upcoming publication. 

#### Track B: Conservation VR Prototype
```
Amph3D Dataset
  ↓
  Unreal Engine Integration
    ├── Underwater Blueprint Environment Build
    ├── Soundscape
    └── Object Interaction
      ↓
      Interactive, Immersive VR Simulation Prototype
```
To make pre-deployment testing more simple and accessible for anyone building machinery that interacts with the marine world, I've created this pipeline which can be made in a short period of time (1-2 days) with limited prior knowledge and limited funds. This pipeline assumes that (if using) a VR device, it is already set up and ready to use with UE5 or UE6. This simulation does not have to be used as a VR environment but if created as such, it can be used for the following purposes:
- Training: fish identification, scuba diving, coral restoration and remote operation of UUVs. 
- Marine biology: practice field studies and wildlife interaction safely prior to conducting expensive and potentially hazardous experiments.
- Education and Conservation
- Accessibility and Therapy
- Gamification

## Tools
| Tool | Type/Version | Source |
|---|---|---|
| ML Model | Segment Anything Model (SAM) | https://github.com/facebookresearch/segment-anything |
| Dataset | Amphitrite v1 | https://doi.org/10.25398/rd.northumbria.28908176 |
| Assets| Underwater Blueprint | Shousha, K. A., 2026|
|| Audio | Tomlija, 2012 |
|| | FxProSound, 2010|
| Software | Meshy.ai (v5/v6) | https://www.meshy.ai/ |
|  | Blender (v4.5) | https://www.blender.org/ |
|  | Unreal Engine (v5/v6) | https://www.unrealengine.com/ |
| Language | Python | https://www.python.org/ |

## Project Structure
- Image-to-3D/
  - Scripts/
    - Group_Render.py
    - Random_Rend.py
  - README.md

## Implementation
More detail on the experimental side is pending a publication.<br> 

### 1. Creating the 3D Dataset
#### Part 1: Segmentation using SAM (Kirillov, 2023)
  - **Step 1**: Take a random selection of images and segment them with SAM. Save as .png files to maintain a transparent background.
  - **Step 2**: Discard any images that have artificial boundaries (ie. cut off from the edge or overlapped).
  
<table align="center">
  <tr>
    <td align="center"><img src="https://github.com/user-attachments/assets/901105ca-6f23-4457-b8e4-237abb04eb80" /></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/8882d799-2845-45fb-8a47-cb4aa27a6c46" /></td>
  </tr>
  <tr>
    <td align="center">Incomplete Segment of Starfish</td>
    <td align="center">Incomplete Segment of Anenome</td>
  </tr>
</table>

#### Part 2: 3D Generation using Meshy
  - **Step 1**: Import the .png file into Meshy.AI. Ensure mesh is watertight and hallucination hasn't occurred.
    - Either repeat Step 1 using the 're-generate' option until the mesh is correct OR the object is too complex and needs to EITHER be disregarded OR re-segmented.

  - **Step 2**: Texture Tweaking in Meshy by choosing the closest texture to the original
     - There is also an option to paint textures onto the mesh with generated prompts such as "add an algae bloom texture" or "add a bright green moss texture" to the masked area.

  - **Step 3**: Export as .obj folders so that they maintain their new textures with the objects and can easily be imported into Blender.

<table align="center">
  <tr>
    <td align="center"><img src="https://github.com/user-attachments/assets/5a9a570d-439c-4aa6-adc5-e84d9c408cfc" /></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/fc6435b8-42e5-4132-8646-bece893e93ec" /></td>
  </tr>
  <tr>
    <td align="center">3D Generated Mesh of a Pot</td>
    <td align="center">Text-to-Image Texture Prompt of Algae</td>
  </tr>
</table>

#### A note on Meshy.ai:
First of all I'm not affiliated with Meshy in any way, I just chose it for it's ability to produce high fidelity/realistic looking meshes with clean topology at a fair price. You do get 100 free credits on a basic account every month and if you are researching or a student you can get a fair deal for 1000 credits a month. That being said, I would spend more time ensuring your segmented topology is clean and not overly complex before importing your image file into meshy, as it may take a few re-generations (which use up credits) to get it correct. There is also an option to re-mesh and lower the poly count which might be applicable for heavily populated environments or low processing power, however, I kept my topology as a high poly count to maintain as much realism as possible. 

### 2A. Rendering for Augmentation (Track A)
#### Part 1: Setting up Cameras
  Step 1: Imported 3D Meshes to Blender 4.5
Now that you can rotate the object with its texture, you can check the quality of both the mesh and the texture. Ensuring no hallucinations, a watertight mesh (where applicable) and an accurate texture.

```
Hint: check any typography/fonts or logos as Meshy can sometimes struggle to replicate this accurately.
```
#### Rendering Uniformly (Recommended for uniform image shots)
The Group_Render.blend script is used here. This script is for a uniform 360 degrees, evenly spaced render around the object.

``` python
output_directory = "/path/directory" # Change to your directory
num_cameras = 8 # How many cameras you'd like to use
camera_distance = 5.0 # Distance of camera away from the object
camera_height = 2.0 # Same as above but height
render_samples = 128 # I chose 16*8 but this is up to you
resolution_x = 1024 # Square images - change dimensions if required
resolution_y = 1024
```

#### Rendering Randomly (Recommended for ML use)
The Random_Render.blend script is used here.
This script is for a 360 degrees render around the object with randomly varying heights, angles and distances to collect information that is harder to overfit to in a machine learning augmentation dataset.


```
Hint: make sure to select the object when you run the render scripts or it won't work. You'll get a printed warning message. 
```
#### Part 2: Rendering with Cycles

#### Render Settings
You can adapt the render settings by opting out of *Cycles*. In this case it was chosen for better lighting on transparent objects (like plastic bags). 

``` python

def setup_render_settings():
    scene = bpy.context.scene #Gets the active scene
    scene.render.engine = 'CYCLES' # Change render engine
    scene.render.image_settings.color_mode = 'RGBA' # Colour profile with transparency
    scene.render.image_settings.file_format = 'PNG' # Change to extension of your choice
    scene.render.film_transparent = True # Change to false if you want a background
 
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/dbef742b-7a25-456a-9442-a04a4ffa0355" alt="Plastic bag 3D generated mesh inside an underwater marine simulation" width="95%" />
</p>

### 2B. An Accessible VR Pipeline (Track B)
[ STEP BY STEP INFO COMING SOON ]

#### Part 1: Integrating Assets
- Importing Blueprint
- Importing Sound
- Importing Assets
#### Part 2: Interaction and Immersion
  Step 1: Transportation </br>
  Step 2: Picking up objects: to easily do this, make sure your object is selected as a *Static Mesh* and add the *Grab Component*. 

```
Physics: For this particular BluePrint, switch 'Simulate Physics' off. (Static Mesh > Physics > Simulate Physics). That means it will just stay where it is when you pick it up. Why? Because the physics of the water system sends the objects up to the surface - so your object will start to float as soon as you enter the environment. Ofcourse, this might be the effect you're going for... 
```
<p align="center">
  <img src="https://github.com/user-attachments/assets/81aa897f-cbba-43ce-a2cb-6ec7b34db089" alt="Elastic band (rubber) 3D generated mesh floating in an underwater marine simulation" width="95%" />
</p>

## Licensing, Copyright and Reusability
The Amphitrite Dataset is stored on Figshare: https://doi.org/10.25398/rd.northumbria.28908176 
<br> License: CC-BY-NC-SA
<br> This requires any users to cite all the authors and obtain permission for individual usage.<br>The dataset is open source for research purposes but it is **not for commercial use**.

As the assets in the VR prototype were used under individual copyright licenses, this simulation is presented strictly as a prototype for academic demonstration. 
<br>Audio (Tomlija, 2012; FxProSound, 2010)
<br>Scene Blueprint (Shousha, 2026) 

## Author
Dr. Zoe Moorton

## References and Citations
FxProSound (2010) "01650 underwater bubbles"  Available at: freesound.org
<br>Kirillov, Alexander; Mintun, Eric; Ravi, Nikhila; Mao, Hanzi; Rolland, Chloe; Gustafson, Laura; Xiao, Tete; Whitehead, Spencer; C. Berg, Alexander;  Lo, Wan-Yen; Dollár, Piotr; Girshick, Ross. (2023) Segment Anything. arxiv
<br>Shousha, K. A. (2026) Underwater_BPV3 PCG coral System. ArtStation.
<br>Tomlija (2012) "A fountain. Slightly resonant. Low." Available at: freesound.org



    