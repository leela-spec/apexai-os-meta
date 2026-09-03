### Optical Mechanics: Crystalline Surface vs. Chamfer Glint

To achieve a glass-and-metal aesthetic without generating a lightsaber streak, the surface wash and the perimeter edges must be rendered as two distinct optical behaviors:

```
[ Ambient Dark Obsidian Glass ]
         │
         ├── Surface Wash: Translucent Specular Pass (Narrower blur, higher clarity, passes through)
         └── 1px Chamfer: Total Internal Refraction (Light concentrates into a vibrant #D51EC4 blade glint)
```

- **Surface Wash (The Glass/Metallic Sheen):** In clean glass, reflections do not scatter 60px wide like milk glass. The reflection is tight ($18\text{px} - 24\text{px}$ falloff) and highly directional. It passes smoothly _through_ the body of the module with low opacity ($12\% - 18\%$) using `mix-blend-mode: overlay` or `color-dodge`, ensuring the amethyst base beneath stays lucid and saturated.
    
- **The Perimeter Glint (Fresnel Chamfer Concentration):** When an incidental light ray hits a 45° beveled chamfer, total internal reflection concentrates that light along the 1px edge. Because this intense specular highlight is physically confined to a 1px stencil, it produces a razor-sharp **blade glint** in brand lila (`#D51EC4`) with a white-hot focal point without spilling over or overwhelming the UI.
    

### Specifications for 3 Clean-Glass Variations

|**Parameter**|**Variation 1: Diamond-Milled Chamfer**|**Variation 2: Anisotropic Katana Streak**|**Variation 3: Lensed Caustic Resonance**|
|---|---|---|---|
|**Aesthetic Goal**|Precision smartphone sapphire glass.|Anime blade sheen across polished titanium.|Fluid liquid glass with organic optical flaring.|
|**Surface Wash Blur**|$22\text{px}$ linear gradient, 15% opacity.|$14\text{px}$ compressed elliptical band.|Dual $28\text{px} / 20\text{px}$ overlapping caustic crests.|
|**Surface Blend Mode**|`overlay` (maintains high crystalline contrast).|`color-dodge` (ignites glass without milky gray).|`screen` over saturated dark amethyst.|
|**1px Edge Intensity**|Concentrated `#D51EC4` with 100% white apex.|Grazing top/top-left chamfer flash only.|Flaring `#D51EC4` bloom strictly at wave intersections.|
|**Kinetic Motion**|Unified screen-space glide (20s cycle).|Sequenced cascade with 3.8s cadence.|Asynchronous harmonic drift (19s / 13s).|

### Implementation Instructions

**1. Diamond-Milled Chamfer (Unified Screen-Space Glint)**

- **The Clean Surface:** Set the global ambient wash to a tighter $140^\circ$ linear gradient: `transparent 45%` $\rightarrow$ `rgba(213, 30, 196, 0.12) 48.5%` $\rightarrow$ `rgba(255, 255, 255, 0.24) 50%` $\rightarrow$ `rgba(213, 30, 196, 0.12) 51.5%` $\rightarrow$ `transparent 55%`. Blur to **22px** (not 58px) with `mix-blend-mode: overlay`.
    
- **The Edge Glint:** Apply a 1px border stencil to every card. Within that 1px track, map the identical screen-space coordinates. Define the traveling edge pulse as: `transparent 48%` $\rightarrow$ `rgba(213, 30, 196, 0.95) 49.5%` $\rightarrow$ `#FFFFFF 50%` $\rightarrow$ `rgba(213, 30, 196, 0.95) 50.5%` $\rightarrow$ `transparent 52%`. Add `filter: drop-shadow(0 0 3px #D51EC4)` strictly to the 1px border layer.
    

**2. Anisotropic Katana Streak (Directional Grazing Chamfer)**

- **The Clean Surface:** Compress the gradient profile into an acute diagonal band ($125^\circ$) with a $16\text{px}$ blur, giving the reflection the sharp falloff of brushed metal or polished crystal.
    
- **Selective Chamfer Masking:** Use an anisotropic mask so only edges facing the light source (the top and top-left chamfers) reflect the highlight, while vertical and bottom boundaries remain at resting `rgba(213, 30, 196, 0.18)`.
    
- **The Glint:** As the sweep crosses each card, fire a 0.4s traveling glint across the top chamfer: a rapid white specular point wrapped in high-saturation `#D51EC4`, illuminating connector SVG paths simultaneously before snapping back to idle.
    

**3. Lensed Caustic Resonance (Dual Wavefront Intersect)**

- **The Clean Surface:** Drive two asynchronous passes across the screen (Wave A at $150^\circ$, 19s period; Wave B at $115^\circ$, 13s period). Tighten their blur values to **24px** to maintain structural presence without fog.
    
- **The Edge Glint:** Render all card perimeters at a quiet baseline stroke of `1px solid rgba(213, 30, 196, 0.20)`.
    
- **Multiplicative Edge Lensing:** Set the overlapping border layer to `mix-blend-mode: color-dodge`. Single waves do not trigger a reaction; only where Wave A and Wave B intersect on a card’s border coordinate does the 1px edge ignite into vibrant `#D51EC4`, casting an 8px crystalline subsurface bleed into the frosted substrate.