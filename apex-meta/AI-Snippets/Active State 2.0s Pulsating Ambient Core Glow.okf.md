# OKF 0.2 Specification: Active State 2.0s Pulsating Ambient Core Glow

yaml

okf_version: "0.2"

spec_id: "DS-GLOW-ACTIVE-001"

title: "Active State Ambient Core Glow & 2.0s Breathing Cadence Specification"

domain: "design_system / visual_effects / skill_tree"

status: "ratified_operator_decision"

target_audience: "AI Design & Implementation Agents (Flutter Canvas, Web/SVG, Shader pipelines)"

---

## 1. Context & Visual Purpose

The **Active State Ambient Core Glow** is an internal, volumetric light source rendered on a dedicated background layer _behind_ a 3D wireframe node (Chunk 1×1, Block 2×2, Epic 3×3). It indicates that a node is the current focus of execution.

+-------------------------------------------------------------------+

|                        RENDERING STACK                            |

|                                                                   |

|  [Layer 3 - Foreground]  Selection Frames / Badges (Leela Lila)   |

|  [Layer 2 - Geometry]    Isometric Wireframe Mesh (Branch Hues)   |

|  [Layer 1 - Luminous]    AMBIENT CORE GLOW (Front-Face Centered)  |

|  [Layer 0 - Background]  Canvas Backdrop (#0B0627 Deep Void)      |

+-------------------------------------------------------------------+

---

## 2. Structural & Semantic Invariants

### 2.1 Invariant: Semantic Branch-Color Binding

- The core glow **MUST** take the node's semantic branch hue. It is **NEVER** generic Leela Purple (`#D36BFF` / `#D51EC4`), which is strictly reserved for interactive selection frames and focus chrome.

|Branch Domain|Token ID|Canonical Hex Code|Glow Base Color|
|---|---|---|---|
|**Physical (P)**|`LeelaTokens.colors.branchPhysical`|`#FF5252`|Coral Red|
|**Mental (M)**|`LeelaTokens.colors.branchMental`|`#40C4FF`|Sky Cyan|
|**Craft (C)**|`LeelaTokens.colors.branchCraft`|`#FFD54F`|Craft Gold|
|**Regeneration (R)**|`LeelaTokens.colors.branchRegen`|`#69F0AE`|Mint Green|
|**Epic Multi-Branch (3×3)**|_Apex / Bridge Branch_|`#FFD54F`|Craft Gold _(or contextual branch)_|

---

## 3. Geometric Center & Sizing Mathematics

In isometric projection with depth ratio dr=0.25dr​=0.25, shear vector (sx=0.70,sy=0.50)(sx​=0.70,sy​=0.50), and face ratio fr=0.62fr​=0.62, the front face is offset by depth shearing to the upper right:

depth=size×0.25,dx=depth×0.70,dy=depth×0.50depth=size×0.25,dx=depth×0.70,dy=depth×0.50 faceW=size×0.62,faceH=size×0.62faceW=size×0.62,faceH=size×0.62 left=size−faceW−dx2,top=size−faceH−dy2+dyleft=2size−faceW−dx​,top=2size−faceH−dy​+dy

### 3.1 Front-Face Centroid Formula

The light source origin (cx,cy)(cx​,cy​) is placed at the exact geometric center of the **front face**:

cx=left+faceW2≈size×0.4125cx​=left+2faceW​≈size×0.4125 cy=top+faceH2≈size×0.5625cy​=top+2faceH​≈size×0.5625

> **Crucial Rule**: Do NOT center at (0.50×size,0.50×size)(0.50×size,0.50×size). Centering on the bounding box causes the glow to drift toward the sheared top/right edges.

### 3.2 Glow Radius Formula

The base radius RglowRglow​ is sized proportionally to the front face width:

Rglow=faceW×0.46≈size×0.285Rglow​=faceW×0.46≈size×0.285

|Canvas Size|faceWfaceW|Center (cx,cy)(cx​,cy​)|Base Radius RglowRglow​|
|---|---|---|---|
|**60 px**|37.2 px37.2 px|(24.75 px,33.75 px)(24.75 px,33.75 px)|17.1 px17.1 px|
|**80 px**|49.6 px49.6 px|(33.00 px,45.00 px)(33.00 px,45.00 px)|22.8 px22.8 px|
|**120 px**|74.4 px74.4 px|(49.50 px,67.50 px)(49.50 px,67.50 px)|34.2 px34.2 px|

---

## 4. Radial Shader & Falloff Calibration

The glow is painted as a 4-stop concentric radial gradient:

Shader(r)=RadialGradient(center=(cx,cy),radius=Rglow)Shader(r)=RadialGradient(center=(cx​,cy​),radius=Rglow​)

α(t)=αbase×pulseFactor(t)where αbase=0.60α(t)=αbase​×pulseFactor(t)where αbase​=0.60

### Luminance Stops Table

|Stop Index|Normalized Radius (r/Rglowr/Rglow​)|Alpha Multiplier|Visual Role|
|---|---|---|---|
|**Stop 1**|`0.00` (0%)|1.00×α(t)1.00×α(t) (≈0.60≈0.60)|Luminous core nucleus|
|**Stop 2**|`0.45` (45%)|0.53×α(t)0.53×α(t) (≈0.32≈0.32)|Warm volumetric midtone|
|**Stop 3**|`0.80` (80%)|0.16×α(t)0.16×α(t) (≈0.10≈0.10)|Atmospheric edge falloff|
|**Stop 4**|`1.00` (100%)|0.000.00 (0.000.00)|Seamless dark background termination|

---

## 5. Temporal Animation: 2.0s Meditative Pulse

The breathing pulse cycles sinusoidally with a **2.0s2.0s (2000ms)** period (0.5 Hz0.5 Hz frequency) to establish a meditative, non-jarring cadence:

pulseValue(t)=1−cos⁡(2πt2.0s)2∈[0.0,1.0]pulseValue(t)=21−cos(2.0s2πt​)​∈[0.0,1.0]

Scale Factor: S(t)=0.94+0.14×pulseValue(t)(Range: 0.94→1.08)Scale Factor: S(t)=0.94+0.14×pulseValue(t)(Range: 0.94→1.08) Opacity Factor: A(t)=0.45+0.50×pulseValue(t)(Range: 0.45→0.95)Opacity Factor: A(t)=0.45+0.50×pulseValue(t)(Range: 0.45→0.95)

Scale / Alpha

 ^

1.08 |                 * * *                 | Peak (t = 1.0s)

1.00 |              *         *              |

0.94 |  * * *                         * * *  | Trough (t = 0.0s, 2.0s)

     +---------------------------------------> Time (s)

        0.0s           1.0s            2.0s

---

## 6. Implementation Reference Blueprints

### 6.1 Flutter Canvas Implementation (`_CoreGlowPainter`)

dart

// 1. Controller setup (2.0s period)

_controller = AnimationController(

  duration: const Duration(milliseconds: 2000),

  vsync: this,

)..repeat(reverse: true);

// 2. CustomPainter execution

void paint(Canvas canvas, Size size) {

  final faceW = size.width * 0.62;

  final faceH = size.height * 0.62;

  final dx = size.width * 0.25 * 0.70;

  final dy = size.width * 0.25 * 0.50;

  final left = (size.width - faceW - dx) / 2;

  final top = (size.height - faceH - dy) / 2 + dy;

  // Front-face centered origin

  final center = Offset(left + faceW / 2, top + faceH / 2);

  final radius = faceW * 0.46;

  // Pulse modulation

  final pulse = 0.94 + animationValue * 0.14;

  final alpha = 0.60 * pulse;

  final paint = Paint()

    ..shader = RadialGradient(

      colors: <Color>[

        branchColor.withValues(alpha: alpha),

        branchColor.withValues(alpha: alpha * 0.53),

        branchColor.withValues(alpha: alpha * 0.16),

        branchColor.withValues(alpha: 0.0),

      ],

      stops: const <double>[0.0, 0.45, 0.80, 1.0],

    ).createShader(Rect.fromCircle(center: center, radius: radius * pulse));

  canvas.drawCircle(center, radius * pulse, paint);

}

### 6.2 SVG / Web CSS Implementation

html

<svg width="80" height="80" viewBox="0 0 80 80">

  <defs>

    <radialGradient id="frontGlow" cx="50%" cy="50%" r="50%">

      <stop offset="0%" stop-color="#FFD54F" stop-opacity="0.60" />

      <stop offset="45%" stop-color="#FFD54F" stop-opacity="0.32" />

      <stop offset="80%" stop-color="#FFD54F" stop-opacity="0.10" />

      <stop offset="100%" stop-color="#FFD54F" stop-opacity="0" />

    </radialGradient>

  </defs>

  <!-- Front face center for size=80: cx=33.0, cy=45.0, r=22.8 -->

  <circle cx="33.0" cy="45.0" r="22.8" 

          fill="url(#frontGlow)" 

          filter="blur(3.2px)"

          style="transform-origin: 33px 45px; animation: front-pulse 2.0s ease-in-out infinite;" />

</svg>

<style>

@keyframes front-pulse {

  0%, 100% { opacity: 0.45; transform: scale(0.94); }

  50%      { opacity: 0.95; transform: scale(1.08); }

}

</style>

---

## 7. Anti-Patterns & Common Traps to Avoid

1. **Top-Left Expansion (Transform Origin Defect)**: In SVG/CSS, never scale an animated circle without explicitly pinning `transform-origin: cx cy`. Default scaling from `(0, 0)` causes the pulse to expand downward and to the right.
2. **Bounding Box Centering Drift**: Never use `(size / 2, size / 2)`. Isometric shear shifts the visual front face downward and leftward relative to the 3D bounding box.
3. **Color Contamination**: Never mix Leela Purple into the core glow of active nodes. Active core light = branch color; UI chrome = purple.