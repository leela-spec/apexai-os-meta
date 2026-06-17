# Discrete Modeling via Boundary Conditional Diffusion Processes

Yuxuan Gu†  Xiaocheng Feng†‡  Lei Huang†  Yingsheng Wu†  Zekun Zhou†  
Weihong Zhong†  Kun Zhu†  Bing Qin†‡  
†Harbin Institute of Technology  ‡ Peng Cheng Laboratory  
{yxgu,xcfeng,lhuang,yswu,zkzhou,whzhong,kzhu,qinb}@ir.hit.edu.cn  

###### Abstract

We present an novel framework for efficiently and effectively extending the powerful continuous diffusion processes to discrete modeling. Previous approaches have suffered from the discrepancy between discrete data and continuous modeling. Our study reveals that the absence of guidance from discrete boundaries in learning probability contours is one of the main reasons. To address this issue, we propose a two-step forward process that first estimates the boundary as a prior distribution and then rescales the forward trajectory to construct a boundary conditional diffusion model. The reverse process is proportionally adjusted to guarantee that the learned contours yield more precise discrete data. Experimental results indicate that our approach achieves strong performance in both language modeling and discrete image generation tasks. In language modeling, our approach surpasses previous state-of-the-art continuous diffusion language models in three translation tasks and a summarization task, while also demonstrating competitive performance compared to auto-regressive transformers. Moreover, our method achieves comparable results to continuous diffusion models when using discrete ordinal pixels and establishes a new state-of-the-art for categorical image generation on the Cifar-10 dataset.

## 1Introduction

Discrete modeling is essential due to the natural prevalence of discreteness in numerous domains, including proteins (Madani et al., [2020](https://arxiv.org/html/2410.22380v1#bib.bib40), [2023](https://arxiv.org/html/2410.22380v1#bib.bib41)), images (Parmar et al., [2018](https://arxiv.org/html/2410.22380v1#bib.bib44); Dosovitskiy et al., [2021](https://arxiv.org/html/2410.22380v1#bib.bib10)), and natural language (Sutskever et al., [2014](https://arxiv.org/html/2410.22380v1#bib.bib54); Brown et al., [2020](https://arxiv.org/html/2410.22380v1#bib.bib4)). Recent dominant framework for discrete modeling is the Transformer (Vaswani et al., [2017](https://arxiv.org/html/2410.22380v1#bib.bib56)) with an autoregressive manner. While achieving impressive performance, it does suffer from a slow step-by-step generation process, especially for long sequences. Continuous Diffusion models (Sohl-Dickstein et al., [2015](https://arxiv.org/html/2410.22380v1#bib.bib50); Ho et al., [2020](https://arxiv.org/html/2410.22380v1#bib.bib24)), on the contrary, exhibit the ability to recover high-dimensional data from noise in parallel with limited iteration steps. Although proved to be effective in continuous data generation (Rombach et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib45); Kong et al., [2021](https://arxiv.org/html/2410.22380v1#bib.bib29)), they continue to encounter challenges in discrete modeling (Austin et al., [2021](https://arxiv.org/html/2410.22380v1#bib.bib3); Chen et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib8); Li et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib31); Gong et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib16)).

In this paper, we reveal a significant discrepancy pertaining to the modeling of discrete data using continuous diffusion models. Current approaches represent a discrete sample with a vector point in the continuous space. The diffusion process learns a neural network to model the probability distributions that recovers this continuous point from Gaussian noise. However, the discrete data actually corresponds to an area in the continuous space rather than a single point, where the oversimplified assumption leads to a mismatch between learned probability contours and the boundary of the discrete area. Take language generation as an example, a word is represented with an embedding vector in the embedding space. To generate this word, it is impractical to strictly enforce the predicted vector to be an exact match to the embedding. On the contrary, vectors around this embedding can also generate the same word, thereby defining the collective area they encompass as a discrete area of this word. As illustrated in Figure [1](https://arxiv.org/html/2410.22380v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")A, suppose the learned probability density function is pθ⁢(𝐱) and two points 𝐱i and 𝐱o are sampled in the same density contour where pθ⁢(𝐱i)=pθ⁢(𝐱o). It is obvious that 𝐱i lies in the discrete area and is able to recover the discrete data while 𝐱o can not. This means that the diffusion model only learns a simplified scenario that does not match the real probability distribution.

![Refer to caption](https://arxiv.org/html/2410.22380v1/x1.png)

Figure 1: (A) Blue and green curves are the learned probability density contours of the diffusion model for two data points. The red area is the discrete area of the blue data 𝐱0 and the boundary of this area is naturally a density contour. The discrete boundary is a complex hypersurface in the high-dimensional continuous space and we simplify it into a red line for convenience of description. As observed in the magnified part, the learned contours deviate from the boundary contour, resulting in inconsistent probability densities and gradient directions. (B) We consider the discrete boundary as priors for the diffusion process to estimate a more appropriate probability distribution, where the learned contours are expected to follow the shape of the discrete boundary.

To address the issues above, we proposed to take the boundaries of discrete areas as priors, as shown in Figure [1](https://arxiv.org/html/2410.22380v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")B, where boundary curves are regarded as oracle contours. As it gradually approaches the discrete boundary, the learned density contours of diffusion models are expected to transform from Gaussian distributions to the boundary distribution. Therefore, we propose to divide the forward process into two steps. First is the boundary estimation where we precisely calculate the stopping time t0 and position 𝐱t0 at which the forward trajectory cross the boundary. Then we rescale the trajectory for both training and inference stages to make the sampling probability of noisy point 𝐱t conditioned on the boundary. To make the boundary estimation tractable ([appendix A](https://arxiv.org/html/2410.22380v1#A1 "Appendix A Stopping Time for Forward Process ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")) and eliminate randomness in conditional state transitions 𝐱t0→𝐱t, we utilize the Ordinary Differential Equations (ODEs) to describe the forward trajectory.

Our approach is experimented in both language modeling and discrete image generation. On three machine translation datasets (Iwslt14 de-en (Cettolo et al., [2012](https://arxiv.org/html/2410.22380v1#bib.bib6)), Wmt14 en-de, Wmt16 en-ro) and a text summarization dataset (Gigaword (Rush et al., [2015](https://arxiv.org/html/2410.22380v1#bib.bib47))) for language modeling, our proposed approach not only significantly improves existing diffusion models to at most 7.8% but also achieves competitive performance to autoregressive transformers. For image generation on Cifar-10 (Krizhevsky et al., [2009](https://arxiv.org/html/2410.22380v1#bib.bib30)), our model realizes a comparable result to continuous diffusion models with discrete ordinal pixels and establishes a new state-of-the-art for categorical pixels.

## 2Preliminaries

#### Diffusion Models

To model a real distribution q⁢(𝐱0), diffusion models utilize a forward process pt⁢(𝐱|𝐱0) with T steps to gradually add Gaussian noise π⁢(𝐱)=𝒩⁢(𝟎,𝐈) into the data distribution, where pT⁢(𝐱|𝐱0)=π⁢(𝐱). There are different architectures for the forward process. A common approach (Ho et al., [2020](https://arxiv.org/html/2410.22380v1#bib.bib24)) considers the forward process as the Markovian process, where pt⁢(𝐱|𝐱0)=∏s=1tps⁢(𝐱s|𝐱s−1) combines a series of Gaussian distributions. Thus the forward process follows a Gaussian distribution that pt⁢(𝐱|𝐱0)=𝒩⁢(α¯t⁢𝐱0,(1−α¯t)⁢𝐈) (Variance Preserving) or pt⁢(𝐱|𝐱0)=𝒩⁢(𝐱0,σt2⁢𝐈) (Variance Exploding) (Song et al., [2021b](https://arxiv.org/html/2410.22380v1#bib.bib52)), where noise scheduler α¯t monotonically decreases from 1 to 0 and σt increases from sufficiently small to the maximum pairwise distance between all training data points. To recover data from noise, diffusion processes train neural networks 𝐱θ⁢(𝐱t,t) to predict 𝐱0 (other equivalent targets include ϵ and ∇log⁡p⁢(𝐱t)) from 𝐱t∼pt⁢(𝐱|𝐱0):

|   |   |   |   |
|---|---|---|---|
||ℒθ=𝔼t∼𝒰(1,T),𝐱0∼q⁢(𝐱0),𝐱t∼pt⁢(𝐱\|𝐱0)⁢[∥𝐱0−𝐱θ⁢(𝐱t,t)∥2].||(1)|

Samples are generated with a series of reverse state transition p⁢(𝐱t−1|𝐱t,𝐱θ⁢(𝐱t,t)).

#### Flow Matching

Another architecture (Lipman et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib34)) utilizes the ODEs and defines a time-dependent flow function ϕt⁢(𝐱)=σt⁢(𝐱0)⁢𝐱+μt⁢(𝐱0) that maps pt⁢(𝐱|𝐱0)=[ϕt]∗⁢π⁢(𝐱)=π⁢(ϕt1⁢(𝐱))⁢|det⁢d⁢ϕt1⁢(𝐱)d⁢𝐱|=𝒩⁢(μt⁢(𝐱0),σt2⁢(𝐱0)⁢𝐈), where μt and σt can be the same as in diffusion models or a more straightforward form that μt=(1−tT)⁢𝐱0 and σt=tT. Recovering data from noises relies on the vector field ut⁢(𝐱|𝐱0) that generates the probability path with the ODE d⁢ϕT−t⁢(𝐱)=uT−t⁢(ϕT−t⁢(𝐱)|𝐱0)⁢d⁢t,t:0→T. Neural networks uθ⁢(𝐱,t) are trained to estimate the vector field ut⁢(𝐱|𝐱0) via the following objective:

|   |   |   |   |
|---|---|---|---|
||ℒθ=𝔼t∼𝒰(1,T),𝐱0∼q⁢(𝐱0),𝐱T∼π⁢(𝐱)⁢[∥uθ⁢(ϕt⁢(𝐱T),t)−d⁢ϕt⁢(𝐱T)d⁢t∥2].||(2)|

Besides, the vector field is proved to have the form:

|   |   |   |   |
|---|---|---|---|
||ut⁢(𝐱\|𝐱0)=σt′⁢(𝐱0)σt⁢(𝐱0)⁢(𝐱−μt⁢(𝐱0))+μt′⁢(𝐱0), where apostrophe indicates derivative to ⁢t.||(3)|

![Refer to caption](https://arxiv.org/html/2410.22380v1/x2.png)

Figure 2:(A) Rescaled Probability Contours. The bold curve 1⁢σ is the density contour of one standard deviation. As the time t decreases from T to 0, the rescaled contours will gradually fit the discrete boundary and probability densities will also concentrate to this boundary. (B) Rescaled Forward Trajectory. Original forward trajectory 𝐱0→𝐱t0→𝐱τ is rescaled to be a boundary conditional trajectory 𝐱~1→𝐱~t that starts from 𝐱~1=𝐱t0. The rescaled forward distribution p~t⁢(𝐱~t|𝐱0) is transformed from the discrete boundary to Gaussian distributions.

## 3Methodology

As illustrated in Figure [2](https://arxiv.org/html/2410.22380v1#S2.F2 "Figure 2 ‣ Flow Matching ‣ 2 Preliminaries ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), our objective is to refine the probability density contours of pt⁢(𝐱|𝐱0) so that they better fit the boundaries of discrete samples while still allowing for the ease of sampling. Let 𝐱0 denote the samples from a real distribution q⁢(𝐱0). Obtaining a boundary-aware corresponding noisy data 𝐱 at time t∈[1,T] is pt⁢(𝐱|𝐱0)=∫pt⁢(𝐱,𝐱t0,t0|𝐱0)⁢d𝐱t0⁢dt0, where t0 is a random variable distributed according to when the diffusion trajectory and the discrete boundary intersect, and 𝐱t0 is the corresponding sample point at t0. Then the forward process is rescaled in two steps:

|   |   |   |   |
|---|---|---|---|
||p~t⁢(𝐱\|𝐱0)=∫p~t⁢(𝐱\|𝐱t0,t0,𝐱0)⏟Trajectory Rescalingp⁢(𝐱t0,t0\|𝐱0)⏟Boundary Estimation⁢d⁢𝐱t0⁢d⁢t0,||(4)|

where the latter term is to calculate the discrete boundaries and the former term is to rescale the forward trajectory. In order to make the equation tractable and ensure that 𝐱 and 𝐱t0 are on the same trajectory, we model the forward process with flow functions ϕt⁢(𝐱) and extend the notation as:

|   |   |   |   |
|---|---|---|---|
||ψt⁢(𝐱)=𝐮⁢(𝐱0,t)⁢𝐱0+𝐯⁢(𝐱0,t)⁢𝐱,pt⁢(𝐱\|𝐱0)=[ψt]∗⁢π⁢(𝐱)||(5)|

where 𝐮⁢(⋅) and 𝐯⁢(⋅) are coefficient functions and sampling 𝐱t from pt⁢(𝐱|𝐱0) equals to

|   |   |   |   |
|---|---|---|---|
||𝐱t=ψt⁢(ϵ),ϵ∼π⁢(𝐱)=𝒩⁢(𝟎,𝐈).||(6)|

### 3.1Estimate Discrete Boundaries

Before figuring out the joint distribution p⁢(𝐱t0,t0|𝐱0), let’s start by discussing how to verify whether an arbitrary point 𝐱 in the continuous space belongs to the discrete area of 𝐱0. Suppose 𝐱0, which exists in the continuous space S, is the representation vector of a discrete random variable ℐ in a discrete space with K states. Besides, 𝒥 is another discrete random variable i.i.d. with ℐ. We define the discrete area of 𝐱0 in the continuous space S as:

|   |   |   |   |
|---|---|---|---|
||Cℐ={∀𝐱∈S\|f⁢(𝐱,ℐ)>f⁢(𝐱,𝒥),∀𝒥≠ℐ},||(7)|

where f⁢(𝐱,ℐ) is a function assessing the likelihood of an arbitrary continuous point 𝐱 inside the discrete area of 𝐱0. For instance, in language modeling, K is the vocabulary size. ℐ,𝒥∈Kn are two different sequences of n tokens and 𝐱0∈ℝ[n,m] is a sequence of m-dimensional vector embeddings for ℐ. f⁢(𝐱,ℐ) is the dot similarity function. Cℐ collects all vectors in the embedding space that will be decoded to generate ℐ and excludes vectors associated with any other token sequences 𝒥.

Given a noisy point 𝐱t0 locating at the boundary between Cℐ and C𝒥, we can get |f⁢(𝐱t0,ℐ)−f⁢(𝐱t0,𝒥)|=0 based on previous definition. Replacing 𝐱t0 with [eqs. 5](https://arxiv.org/html/2410.22380v1#S3.E5 "In 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and [6](https://arxiv.org/html/2410.22380v1#S3.E6 "Equation 6 ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), there is:

|   |   |   |   |
|---|---|---|---|
||f⁢(𝐮t0⁢𝐱0+𝐯t0⁢ϵ,ℐ)=f⁢(𝐮t0⁢𝐱0+𝐯t0⁢ϵ,𝒥).||(8)|

In language modeling and categorical images, f⁢(⋅) is a linear projection function that:

|   |   |   |   |
|---|---|---|---|
||𝐮t0⁢(f⁢(𝐱0,ℐ)−f⁢(𝐱0,𝒥))=𝐯t0⁢(f⁢(ϵ,𝒥)−f⁢(ϵ,ℐ)).||(9)|

Further simplification of this equation can not be universally applied to all arbitrary forms of 𝐮t0 and 𝐯t0. Therefore, we calculate separately for several commonly occurring special cases.

#### Diffusion Process

For variance preserving, there is 𝐮t2+𝐯t2=1 and we have:

|   |   |   |   |
|---|---|---|---|
||𝐮t0=1/1+(f⁢(𝐱0,ℐ)−f⁢(𝐱0,𝒥)f⁢(ϵ,𝒥)−f⁢(ϵ,ℐ))2⁢ and ⁢𝐯t0=1/1+(f⁢(ϵ,𝒥)−f⁢(ϵ,ℐ)f⁢(𝐱0,ℐ)−f⁢(𝐱0,𝒥))2.||(10)|

For variance exploding, there are 𝐮t=1 and 𝐯t=σt. We can obtain:

|   |   |   |   |
|---|---|---|---|
||𝐮t0=1⁢ and ⁢𝐯t0=(f⁢(ϵ,𝒥)−f⁢(ϵ,ℐ))/(f⁢(𝐱0,ℐ)−f⁢(𝐱0,𝒥)).||(11)|

#### Flow Matching

For optimal transport, there is 𝐮t+𝐯t=1 and similarly we get:

|   |   |   |   |
|---|---|---|---|
||𝐮t0=1/(1+f⁢(𝐱0,ℐ)−f⁢(𝐱0,𝒥)f⁢(ϵ,𝒥)−f⁢(ϵ,ℐ))⁢ and ⁢𝐯t0=1/(1+f⁢(ϵ,𝒥)−f⁢(ϵ,ℐ)f⁢(𝐱0,ℐ)−f⁢(𝐱0,𝒥)).||(12)|

As a result, t0 can be directly derived by inverting the coefficient function 𝐮t or 𝐯t, which depends on the choice of noise scheduling strategies. Since their differences do not affect our results, we omit the detailed calculation ([appendix E](https://arxiv.org/html/2410.22380v1#A5 "Appendix E Details of the Function 𝐺 ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")) and denote this process with a function G⁢(⋅):

|   |   |   |   |
|---|---|---|---|
||t0=G⁢(𝐱0,ϵ), where ⁢𝐮⁢(𝐱0,G⁢(𝐱0,ϵ))=𝐮t0⁢ and ⁢𝐯⁢(𝐱0,G⁢(𝐱0,ϵ))=𝐯t0.||(13)|

It’s worth noting that t0 is not a scalar but a vector, where the dimension is the number of elements in 𝐱0. If 𝐱0 is a sequence of n tokens, t0∈[1,T]n. If 𝐱0 is a RGB image with 3-channel × h-height × w-width of pixels, t0∈[1,T]3×h×w. Furthermore, the corresponding noisy sample 𝐱t0 is derived as:

|   |   |   |   |
|---|---|---|---|
||𝐱t0=𝐮⁢(𝐱0,G⁢(𝐱0,ϵ))⁢𝐱0+𝐯⁢(𝐱0,G⁢(𝐱0,ϵ))⁢ϵ=ψG⁢(𝐱0,ϵ)⁢(ϵ),||(14)|

which is a time-independent function of the Gaussian noise ϵ. It’s worth mentioning that both p⁢(t0|𝐱0) and p⁢(𝐱t0|𝐱0) are intractable, since G⁢(𝐱0,ϵ) and ψG⁢(𝐱0,ϵ)⁢(ϵ) are not invertible to ϵ. Different ϵs can be mapped to a same t0 or 𝐱t0. Fortunately, there is an one-to-one mapping between ϵ and the [𝐱t0;t0] pair. We denote the boundary flow function and the corresponding inversion as

|   |   |   |   |
|---|---|---|---|
||Ψ⁢(ϵ)=[ψG⁢(𝐱0,ϵ)⁢(ϵ);G⁢(𝐱0,ϵ)],Ψ1⁢([𝐱t0;t0])=(𝐱t0−𝐮⁢(𝐱0,t0)⁢𝐱0)/𝐯⁢(𝐱0,t0),||(15)|

and the joint boundary distribution is calculated as

|   |   |   |   |
|---|---|---|---|
||p⁢(𝐱t0,t0\|𝐱0)=[Ψ]∗⁢π⁢([𝐱t0;t0]).||(16)|

The support set of 𝐱t0 is restricted to the boundary contour, while other regions in the space are assigned a probability of 0. To obtain the complete boundary, it is necessary to iterate over all possible choices of 𝒥 and perform pairwise comparisons with ℐ. The complexity is O⁢(n×K), where n elements in 𝐱0 is independently iterated. In practical implementation, obtaining the tightest boundary only requires one step of parallel calculation and an extra min⁡(⋅) function over all t0 candidates.

#### Confidence Factor

The discrete area defined by [eq. 7](https://arxiv.org/html/2410.22380v1#S3.E7 "In 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") represents an ideal scenario in which the confidence of the boundary is insufficiently reliable for practical application. Due to the intractability of obtaining the probability density function across the entire discrete area and calculating its confidence interval, we employ an empirical strategy. This approach involves utilizing a confidence factor, denoted as r, ranging from 0 to 1, which is multiplied by t0 to strike a balance between confidence and discreteness. Therefore, r=0 implies the exclusion of discrete priors, causing the discrete area to collapse into a single point, which is the original diffusion process. As the value of r increases, the modeling of discrete boundaries improves at the expense of reliability. Empirically, when the model is conditioned with good guidance, setting a larger value for r allows us to obtain better discrete priors. However, in the case of unconditional modeling, maintaining reliability becomes more crucial to prevent oscillations and even collapses during training.

### 3.2Rescale the Forward Trajectory

In this section, we introduce how to formulate the forward trajectory conditioned on discrete boundaries and derive the rescaled noisy sampling distribution. We start with the boundary-independent forward process pt⁢(𝐱|𝐱0). Let 𝐱t denote a noisy point at time t sampled from pt⁢(𝐱|𝐱0), there is ϵt=(𝐱t−𝐮⁢(𝐱0,t)⁢𝐱0)/𝐯⁢(𝐱0,t) given [eq. 5](https://arxiv.org/html/2410.22380v1#S3.E5 "In 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"). [Equations 14](https://arxiv.org/html/2410.22380v1#S3.E14 "In Flow Matching ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and [13](https://arxiv.org/html/2410.22380v1#S3.E13 "Equation 13 ‣ Flow Matching ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") provide the corresponding [𝐱t0;t0] pair on the same trajectory, which is deterministically calculated with no randomness:

|   |   |   |   |
|---|---|---|---|
||[𝐱t0;t0]=Ψ⁢(ϵt), where ⁢ϵt=(𝐱t−𝐮⁢(𝐱0,t)⁢𝐱0)/𝐯⁢(𝐱0,t).||(17)|

To model the transition probability pt⁢(𝐱t0,t0|𝐱t,𝐱0), we utilize the Dirac delta function δ⁢(𝐱)≃limσ→0𝒩⁢(𝟎,σ2⁢𝐈), which can be loosely thought of as aggregating all probability densities toward the origin, assigning an infinite density at the origin and zero densities elsewhere. Therefore, we have pt⁢(𝐱t0,t0|𝐱t,𝐱0)=δ⁢([𝐱t0;t0]−Ψ⁢(ϵt)). Then the forward process, conditioned on the discrete boundary, is simply derived via Bayes’ rule:

|   |   |   |   |
|---|---|---|---|
||pt(𝐱t\|𝐱t0,t0,𝐱0)=pt(𝐱t0,t0\|𝐱t,𝐱0)pt⁢(𝐱t\|𝐱0)p⁢(𝐱t0,t0\|𝐱0)={0,[𝐱t0;t0]≠Ψ⁢(ϵt)+∞×pt⁢(𝐱t\|𝐱0)p⁢(𝐱t0,t0\|𝐱0),otherwise.||(18)|

Since pt⁢(𝐱t|𝐱0)>0 and p⁢(𝐱t0,t0|𝐱0)>0, pt⁢(𝐱t|𝐱t0,t0,𝐱0) is also a delta function that

|   |   |   |   |
|---|---|---|---|
||pt⁢(𝐱t\|𝐱t0,t0,𝐱0)=δ⁢(𝐱t−𝐮⁢(𝐱0,t)⁢𝐱0−𝐯⁢(𝐱0,t)⁢Ψ1⁢([𝐱t0;t0])).||(19)|

Based on the translation property of the Dirac delta function, i.e. ∫f⁢(x)⁢δ⁢(x−a)⁢dx=f⁢(a), the original forward process pt⁢(𝐱t|𝐱0)=[ψt∘Ψ1∘Ψ]∗⁢π⁢(𝐱t)=[ψt]∗⁢π⁢(𝐱t) naturally ignores the influence of discrete boundaries, even if the boundary information is explicitly added as a condition.

To enable the discrete priors, we propose a simple and intuitive approach: rescale the forward trajectory. As shown in Figure [2](https://arxiv.org/html/2410.22380v1#S2.F2 "Figure 2 ‣ Flow Matching ‣ 2 Preliminaries ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")B, the original forward process flows from 𝐱0 to a random noise ϵ, and we reset the starting point to 𝐱t0. Accordingly, the intermediate noisy points 𝐱t,t∈[1,T] will be proportionally mapped on this new path, which is

|   |   |   |   |   |
|---|---|---|---|---|
||𝐱~t|=𝐱τ,τ=𝒯⁢(t,t0)=r×t0+t×(T−r×t0)/T||(20)|
|||=𝐮⁢(𝐱0,𝒯⁢(t,t0))⁢𝐱0+𝐯⁢(𝐱0,𝒯⁢(t,t0))⁢Ψ1⁢([𝐱t0;t0]).||

Similar to [eq. 19](https://arxiv.org/html/2410.22380v1#S3.E19 "In 3.2 Rescale the Forward Trajectory ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), the rescaled conditional forward process is a Dirac delta function:

|   |   |   |   |
|---|---|---|---|
||p~t⁢(𝐱~t\|𝐱t0,t0,𝐱0)=δ⁢(𝐱~t−𝐮⁢(𝐱0,𝒯⁢(t,t0))⁢𝐱0−𝐯⁢(𝐱0,𝒯⁢(t,t0))⁢Ψ1⁢([𝐱t0;t0])).||(21)|

However, p~t⁢(𝐱~t|𝐱0) faces the same problem of irreversibility as in [eq. 14](https://arxiv.org/html/2410.22380v1#S3.E14 "In Flow Matching ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and we derive it as:

|   |   |   |   |   |
|---|---|---|---|---|
||p~t⁢(𝐱~t\|𝐱0)|=∫p~t⁢(𝐱~t,τ\|𝐱0)⁢dτ=∫p~t⁢(𝐱~t,τ\|𝐱t0,t0,𝐱0)⁢p⁢(𝐱t0,t0\|𝐱0)⁢d⁢[𝐱t0;t0]⁢dτ||(22)|
|||=∫[ψτ∘Ψ1∘Ψ]∗⁢π⁢([𝐱~t;τ])⁢dτ=∫[ψτ]∗⁢π⁢([𝐱~t;τ])⁢dτ.||

Obtaining the probability density function requires gathering together the probability densities of the same location 𝐱~t with different τ, which is intractable. Fortunately, we only need to sample noiy points from this probability distribution 𝐱~t∼p~t⁢(𝐱~t|𝐱0), which is easy to implement:

|   |   |   |   |
|---|---|---|---|
||𝐱~t=𝐮⁢(𝐱0,𝒯⁢(t,G⁢(𝐱0,ϵ)))⁢𝐱0+𝐯⁢(𝐱0,𝒯⁢(t,G⁢(𝐱0,ϵ)))⁢ϵ,ϵ∼π⁢(𝐱).||(23)|

### 3.3Recover Data from Noise

#### Training Objective

Algorithm 1 Training

1:  repeat

2:     𝐱0∼q⁢(𝐱0), ϵ∼π⁢(𝐱)=𝒩⁢(𝟎,𝐈)

3:     t∼Uniform⁢({1,…,T})

4:     τ≔𝒯⁢(t,G⁢(𝐱0,ϵ))// [eqs. 13](https://arxiv.org/html/2410.22380v1#S3.E13 "In Flow Matching ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and [20](https://arxiv.org/html/2410.22380v1#S3.E20 "Equation 20 ‣ 3.2 Rescale the Forward Trajectory ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")

5:     𝐱~t≔𝐮⁢(𝐱0,τ)⁢𝐱0+𝐯⁢(𝐱0,τ)⁢ϵ// [eq. 23](https://arxiv.org/html/2410.22380v1#S3.E23 "In 3.2 Rescale the Forward Trajectory ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")

6:     Take gradient descent step on   ∇θ⁢‖𝐱0−𝐱θ⁢(𝐱~t,t)‖2// [eq. 24](https://arxiv.org/html/2410.22380v1#S3.E24 "In Training Objective ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")

7:  until converged

Theoretically, the diffusion neural networks can be trained as in [eq. 2](https://arxiv.org/html/2410.22380v1#S2.E2 "In Flow Matching ‣ 2 Preliminaries ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), where the rescaled vector field is derived as u~t=d⁢𝐱~td⁢t=d⁢𝐱~td⁢τ⁢d⁢τd⁢t. However, since a low error estimation on 𝐱0 is of significant importance to our trajectory rescaling method, according to [eqs. 10](https://arxiv.org/html/2410.22380v1#S3.E10 "In Diffusion Process ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), [11](https://arxiv.org/html/2410.22380v1#S3.E11 "Equation 11 ‣ Diffusion Process ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), [12](https://arxiv.org/html/2410.22380v1#S3.E12 "Equation 12 ‣ Flow Matching ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and [13](https://arxiv.org/html/2410.22380v1#S3.E13 "Equation 13 ‣ Flow Matching ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), we convert the objective to an upper bound of the [eq. 2](https://arxiv.org/html/2410.22380v1#S2.E2 "In Flow Matching ‣ 2 Preliminaries ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") (See [appendix F](https://arxiv.org/html/2410.22380v1#A6 "Appendix F Details of the Training Objective ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") for more details) and train a neural network 𝐱θ⁢(𝐱~t,t) to predict 𝐱0 directly:

|   |   |   |   |
|---|---|---|---|
||ℒθ=𝔼𝐱0∼q⁢(𝐱0),t∼𝒰(1,T),𝐱~t∼p~t⁢(𝐱\|𝐱0)⁢[∥𝐱0−𝐱θ⁢(𝐱~t,t)∥2].||(24)|

The training procedure is demonstrated in [algorithm 1](https://arxiv.org/html/2410.22380v1#alg1 "In Training Objective ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and key steps are summarized in the line [4](https://arxiv.org/html/2410.22380v1#alg1.l4 "In Algorithm 1 ‣ Training Objective ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes").

#### Reverse Process

Algorithm 2 Sampling

1:  t≔T, τ≔T

2:  ϵ^≃𝐱~t∼𝒩⁢(𝟎,𝐈)// Initialing

3:  for Δ⁢t≔Δ⁢t1,…,Δ⁢ts do // ∑Δ⁢t=T

4:     𝐱^0≔𝐱θ⁢(𝐱~t,t)// Pseudo Target

5:     t≔t−Δ⁢t// Updating

6:     τ≔𝒯⁢(t,G⁢(𝐱^0,ϵ^))// [eq. 25](https://arxiv.org/html/2410.22380v1#S3.E25 "In Reverse Process ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")

7:     𝐱~t≔𝐮⁢(𝐱^0,τ)⁢𝐱^0+𝐯⁢(𝐱^0,τ)⁢ϵ^

8:     ϵ^≔Ψ1⁢([𝐱~t;τ])// Trajectory Alteration

9:  end for

10:  𝐱0≔𝐱θ⁢(𝐱~t,t)// 𝐱1→𝐱0

11:  return 𝐱0

A direct approach that follows the flow matching is to solve the ODE of d⁢ψT−t⁢(𝐱)=u~T−t⁢(ψT−t⁢(𝐱)|𝐱0)⁢d⁢t,ψT⁢(𝐱)∼π⁢(𝐱). This form of transformation is inefficient with 𝐱0-prediction during inference because we have to solve the equation of τ=𝒯⁢(t,G⁢(𝐱θ,𝐱~t−𝐮⁢(𝐱θ,τ)⁢𝐱θ𝐯⁢(𝐱θ,τ))) to get the τ with respect to the change of 𝐱~t and 𝐱θ in real time. Therefore, we provide a deterministic reverse process as an alternative, which is a special case of DDIM (Song et al., [2021a](https://arxiv.org/html/2410.22380v1#bib.bib51)) or the ODE with discrete timesteps. Given the time intervals Δ⁢t∈[Δ⁢t1,…⁢Δ⁢ts],∑Δ⁢t=T , we generalize the boundary conditions [𝐱t0;t0] in p~t⁢(𝐱~t|𝐱t0,t0,𝐱0) of [eq. 21](https://arxiv.org/html/2410.22380v1#S3.E21 "In 3.2 Rescale the Forward Trajectory ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and Ψ1⁢([𝐱t0;t0]) of [eq. 15](https://arxiv.org/html/2410.22380v1#S3.E15 "In Flow Matching ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") to any arbitrary condition pairs [𝐱~t;τ] and obtain the reverse process:

|   |   |   |   |   |
|---|---|---|---|---|
|||p~⁢([𝐱~t−Δ⁢t;τΔ]\|[𝐱~t;τ],𝐱^0)=||(25)|
|||δ⁢([𝐱~t−Δ⁢tτΔ]−[𝐮⁢(𝐱^0,τΔ)⁢𝐱^0+𝐯⁢(𝐱^0,τΔ)⁢ϵ^𝒯⁢(t−Δ⁢t,G⁢(𝐱^0,ϵ^))]),||

where 𝐱^0=𝐱θ⁢(𝐱~t,t) and τΔ is the previous timestep of τ on the same rescaled trajectory.

Sampling from the reverse process is illustrated in [algorithm 2](https://arxiv.org/html/2410.22380v1#alg2 "In Reverse Process ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"). Similar to the sampling process of DDIM (Song et al., [2021a](https://arxiv.org/html/2410.22380v1#bib.bib51)), it starts from the Gaussian noise, iteratively predicts the pseudo target 𝐱^0, and updates the reverse trajectory. However, since the τ and ϵ^ are mutually conditioned, we have to keep track of the t, τ, 𝐱~t, and ϵ^ during each iteration and split the update of ϵ^ into an asynchronous step (line [8](https://arxiv.org/html/2410.22380v1#alg2.l8 "In Algorithm 2 ‣ Reverse Process ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")). Because reverse trajectory keeps changing due to different pseudo targets 𝐱^0 predicted by learned neural networks, which brings severe instability, sometimes simply fixing the initial path (removing the line [8](https://arxiv.org/html/2410.22380v1#alg2.l8 "In Algorithm 2 ‣ Reverse Process ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")) exhibits better performance in experiments.

## 4Language Modeling

Recent diffusion language models (Li et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib31); Gong et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib16)) inherit the embedding-rounding framework that a sentence with n discrete tokens W=[w1,…,wn] is embedded to a continuous space via a trainable embedding layer Emb⁢(W)=[Emb⁢(w1),…,Emb⁢(wn)]. The vocabulary set is K that ∀wn∈K. Besides, the token embeddings are used as the target points 𝐱0=[𝐱01,…,𝐱0n], 𝐱0n=Emb⁢(wn), for continuous diffusion trajectories. Hence, generating tokens from embeddings is:

|   |   |   |   |
|---|---|---|---|
||p⁢(W\|𝐱0)=∑i=1np⁢(wi\|𝐱0i)=∑i=1nexp⁡(f⁢(𝐱0i,wi))∑j∈Kexp⁡(f⁢(𝐱0i,j)),||(26)|

where f⁢(𝐱,j)=Emb⁢(j)⋅𝐱 is the dot production distance. It’s also the function assessing the likelihood of point 𝐱 inside the discrete area of j. The coefficient functions follow the DDPM (Ho et al., [2020](https://arxiv.org/html/2410.22380v1#bib.bib24)), which are 𝐮⁢(𝐱0,t)=α¯t and 𝐯⁢(𝐱0,t)=1−α¯t. Besides, the objectives are

|   |   |   |   |
|---|---|---|---|
||ℒθ=𝔼W,t,𝐱~t⁢[∑i=1n∥Emb⁢(wi)−𝐱θ⁢(𝐱~ti,t)∥2/n]||(27)|

and an additional rounding objective, which is commonly used in language modeling,

|   |   |   |   |   |
|---|---|---|---|---|
|||ℒr=−log⁡pθ⁢(W\|𝐱0)=−log⁡pθ⁢(W\|𝐱θ⁢(𝐱~t,t)).||(28)|

The final training target is given by ℒ=ℒθ+ℒr, where the 𝐱0 of the same token sequence W keeps changing because the embedding layer Emb is trainable, which makes the model hard to be trained. Since previous work does not model discrete areas, a large number of noisy samples inside this area will make ℒr too small to guide the training of the embedding layer, leading to a mode collapse.

#### Experimental Setup

Datasets used for experiments include three translation tasks (Iwslt14 de-en (Cettolo et al., [2012](https://arxiv.org/html/2410.22380v1#bib.bib6)), Wmt14 en-de, and Wmt16 en-ro11[https://github.com/shawnkx/Fully-NAT](https://github.com/shawnkx/Fully-NAT)) and one text summarization task (Gigaword  (Rush et al., [2015](https://arxiv.org/html/2410.22380v1#bib.bib47))). We mainly follow the setting of Gao et al. ([2022](https://arxiv.org/html/2410.22380v1#bib.bib13)), which is inherited from previous non-auto-regressive text generation works (Gu et al., [2018](https://arxiv.org/html/2410.22380v1#bib.bib17), [2019](https://arxiv.org/html/2410.22380v1#bib.bib18); Ghazvininejad et al., [2019](https://arxiv.org/html/2410.22380v1#bib.bib14)), where translation datasets are distilled (Kim and Rush, [2016](https://arxiv.org/html/2410.22380v1#bib.bib27)). Baselines are mainly continuous diffusion language models. DiffuSeq (Gong et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib16)) and SeqDiffuSeq (Yuan et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib58)) are derived from Diffusion-LM (Li et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib31)). Difformer (Gao et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib13)) and Dinoiser (Ye et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib57)) are recent empirical studies highlighting that scaling up the noise is beneficial for language modeling. We also compare with discrete diffusion language models, including D3PM (Austin et al., [2021](https://arxiv.org/html/2410.22380v1#bib.bib3)) and SEDD (Lou et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib37)). Since SEDD is a pre-trained language model, we configure its framework and train it from scratch specifically for our tasks. In addition, auto-regressive transformer (Vaswani et al., [2017](https://arxiv.org/html/2410.22380v1#bib.bib56)) is still one of the most powerful architectures for language generation.

Our boundary conditional diffusion language model is constructed from Difformer (Gao et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib13)), where the model configuration is transformer-iwslt-de-en in Fairseq framework (Ott et al., [2019](https://arxiv.org/html/2410.22380v1#bib.bib42)) for Iwslt14 de-en and transformer-base for other datasets. Sentences are tokenized with Byte-Pair Encoding (Sennrich et al., [2016](https://arxiv.org/html/2410.22380v1#bib.bib49)) and evaluated by detokenized Bleu (Papineni et al., [2002](https://arxiv.org/html/2410.22380v1#bib.bib43)) for machine translation and Rouge (Lin, [2004](https://arxiv.org/html/2410.22380v1#bib.bib32)) for summarization. During training, the diffusion step is T=2000 and the confidence factor r=1 for translation tasks since they have strong conditions, while r=0.5 for summarization. Sentences are generated deterministically with 20 steps.

Table 1:Result of Bleu scores on machine translation and Rouge scores on text summarization.

|   |   |   |   |   |
|---|---|---|---|---|
|Models|Iwslt14 de-en|Wmt14 en-de|Wmt16 en-ro|Gigaword|
|Bleu <br><br>(Bleu-1/2/3/4)<br><br> ⇑|Bleu <br><br>(Bleu-1/2/3/4)<br><br> ⇑|Bleu <br><br>(Bleu-1/2/3/4)<br><br> ⇑|Rouge-1/2/L⇑|
|Auto-Regressive Modeling|   |   |   |   |
|Transformers|34.31 <br><br>(67.3/41.6/27.9/19.1)|28.01 <br><br>(58.2/33.5/21.7/14.6)|34.05 <br><br>(63.1/39.9/27.6/19.6)|37.57/18.90/34.69|
|Ours+Rerank|35.02 <br><br>(68.7/43.3/29.2/20.1)|27.67 <br><br>(57.9/33.2/21.4/14.3)|34.33 <br><br>(63.1/40.1/27.8/19.8)|37.49/18.68/34.82|
|Diffusion Process|   |   |   |   |
|D3PM|27.61 <br><br>(65.4/37.7/22.8/14.2)|22.94 <br><br>(54.9/28.8/16.9/10.4)|27.84 <br><br>(59.8/34.9/22.1/14.5)|33.92/14.96/31.72|
|DiffuSeq|28.78 <br><br>( -/-/-/- )|15.37 <br><br>( -/-/-/- )|25.45 <br><br>( -/-/-/- )|31.17/12.23/29.24|
|SeqDiffuSeq|30.03 <br><br>( -/-/-/- )|17.14 <br><br>( -/-/-/- )|26.17 <br><br>( -/-/-/- )|31.90/12.36/29.22|
|Difformer|31.58 <br><br>(68.6/41.4/26.7/17.5)|24.80 <br><br>(58.7/32.0/19.7/12.5)|30.08 <br><br>(64.4/39.5/26.5/18.2)|35.47/15.17/32.82|
|SEDD|31.87 <br><br>(68.7/41.8/27.2/18.0)|24.98 <br><br>(59.2/32.4/20.1/12.9)|29.38 <br><br>(62.2/38.0/24.9/16.9)|34.33/15.22/32.06|
|Dinoiser|31.91 <br><br>(67.1/40.9/26.7/17.7)|24.77 <br><br>(57.2/31.0/19.0/12.0)|31.49 <br><br>(62.8/38.4/25.5/17.3)|35.17/15.63/32.53|
|Ours|33.42 <br><br>(68.0/42.0/27.7/18.6)|26.69 <br><br>(57.7/32.3/20.4/13.4)|33.15 <br><br>(63.4/39.9/27.4/19.2)|36.44/16.09/33.56|

#### Results

Performances are demonstrated in Table [1](https://arxiv.org/html/2410.22380v1#S4.T1 "Table 1 ‣ Experimental Setup ‣ 4 Language Modeling ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"). Our approach achieves the state-of-the-art compared with continuous diffusion language models and outperforms the two discrete baselines on three machine translation and one text summarization tasks. Our method shows advantages, with a 73.6% significant improvement at most on Wmt14 en-de, over DiffuSeq (Gong et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib16)) and SeqDiffuSeq (Yuan et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib58)), which are two basic methods directly applying diffusion process to language modeling. Compared with recent strong diffusion language models like Difformer (Gao et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib13)) and Dinoiser (Ye et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib57)), which have deployed various effective noise scheduling strategies on diffusion processes from the empirical perspective, our model is still superior with at most 3.07 advancement of Bleu score on Wmt16 en-ro. This implies the effectiveness of modeling discrete priors. In addition, we illustrate the performance of auto-regressive modeling, where we use the transformer (Vaswani et al., [2017](https://arxiv.org/html/2410.22380v1#bib.bib56)) to rerank the generated sentence candidates (7 length beam × 3 sentence beams) of our model. The reranked performance can even outperform transformers on Iwslt14 de-en and Wmt16 en-ro.

Table 2:Ablation studies.

|Models|Iwslt14|Wmt16|
|---|---|---|
|Base (Difformer)|31.58|30.08|
|+ forward only|33.02|32.86|
|+ forward & reverse|33.42|33.15|
|Optimal Transport|32.77|33.65|

#### Ablation

Our approach is a general framework applicable to almost all continuous diffusion models, providing them with discrete boundaries as priors. We choose Difformer (Gao et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib13)) as the base model and follow the configurations. As proved in [eq. 19](https://arxiv.org/html/2410.22380v1#S3.E19 "In 3.2 Rescale the Forward Trajectory ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), the original forward process will ignore the discrete priors although explicitly demonstrated. We conduct ablation experiments on the rescaling module. As illustrated in [Table 2](https://arxiv.org/html/2410.22380v1#S4.T2 "In Results ‣ 4 Language Modeling ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), our approach rescales the trajectory of both forward and reverse processes on Difformer. Only rescaling the forward trajectory is also effective but sub-optimal due to the inconsistent distribution during inference. Due to computational cost and fair comparison, our method leaves room for improvement. For example, replacing the forward trajectory with optimal transport in Flow Matching, 𝐮⁢(𝐱0,t)=1−t/T and 𝐯⁢(𝐱0,t)=t/T, achieves better performance on Wmt16.

Table 3:Analysis on the training objectives.

|Objectives|𝔼𝐱~t⁢∥𝐱0−𝐱^0∥2|𝔼𝐱~t⁢∥u~t⁢(𝐱~t\|𝐱0)−u~t⁢(𝐱~t\|𝐱^0)∥2|𝔼𝐱~t⁢[p⁢(𝐱^0∈C𝐱0)]|Bleu|
|---|---|---|---|---|
|ℒ𝐱0 (eq. [24](https://arxiv.org/html/2410.22380v1#S3.E24 "Equation 24 ‣ Training Objective ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"))|8.44|1.56|51.81%|33.42|
|ℒu~t|8.41|1.55|52.34%|33.49|

#### Analysis

Our training objective, [eq. 24](https://arxiv.org/html/2410.22380v1#S3.E24 "In Training Objective ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), is an upper bound of the [eq. 2](https://arxiv.org/html/2410.22380v1#S2.E2 "In Flow Matching ‣ 2 Preliminaries ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"). We demonstrate the influence of this approximation in [Table 3](https://arxiv.org/html/2410.22380v1#S4.T3 "In Ablation ‣ 4 Language Modeling ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") on Iwslt14 de-en to reveal the thought of our formula. On the one hand, ℒ𝐱0 brings theoretical errors at a constant scale. On the other hand, ℒ𝐱0 mitigates some experimental errors from the neural networks. The first row ℒ𝐱0 is the objective we used in [eq. 24](https://arxiv.org/html/2410.22380v1#S3.E24 "In Training Objective ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and the second row ℒu~t=𝔼{t,𝐱0,𝐱~t}⁢[∥u~t⁢(𝐱~t|𝐱θ⁢(𝐱~t,t))−d⁢𝐱~td⁢t∥2] is directly derived from the [eq. 2](https://arxiv.org/html/2410.22380v1#S2.E2 "In Flow Matching ‣ 2 Preliminaries ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"). The first two columns represent the error expectations of 𝐱0 and u~t on the test set. It is easy to observe that, with the dynamic coefficient d⁢τd⁢t=T−r×G⁢(𝐱0,ϵ)T ([appendix F](https://arxiv.org/html/2410.22380v1#A6 "Appendix F Details of the Training Objective ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")), the value of 𝐱0’s error (8.44) is much larger than the u~t’s error (1.56). Therefore, ℒ𝐱0 is beneficial for reducing the impact of the prediction error from the neural network. The third column in [Table 3](https://arxiv.org/html/2410.22380v1#S4.T3 "In Ablation ‣ 4 Language Modeling ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") illustrates the one-step accuracy of predicting 𝐱0 and the fourth column is the Bleu score on the test set. Experimental results show that optimizing the upper bound has a negligible impact on the final performance (only a 0.2% drop of the Bleu score), while can improve the efficiency of the loss calculation during the training phase.

## 5Discrete Image Generation

Image pixels are usually treated as real numbers in continuous space since adjacent pixel values exhibit linear continuity.They are essentially discrete and quantized data with a finite state space, such as 256 states in RGB format. We utilize two discrete image representations. One is binary coding provided by Bit Diffusion (Chen et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib8)) that converts a sub-pixel with 256 integers to a 8-bit binary code. It is more efficient as it stores ordinal relationships, but the representation space it constructs will be sparse. Another is pixel embedding, which is a more discrete form of representation because the relationships between pixels are thoroughly broken down and reconstructed by learning the embedding representation. Each pixel is regarded as a one-hot vector and transformed with an embedding layer Emb as used in language. Furthermore, we design an intermediate state to demonstrate the correlation between discreteness and modeling difficulty, which is initializing a fixed embedding with binary coding. The optimization target for binary coding is the MSE loss, and pixel embeddings take the same objective as in language.

#### Experimental Setup

We use Cifar-10 (Krizhevsky et al., [2009](https://arxiv.org/html/2410.22380v1#bib.bib30)) for discrete image generation. The evaluation metric is Fid (Heusel et al., [2017](https://arxiv.org/html/2410.22380v1#bib.bib22)), which compares 50K generated samples with the training set. Our image generation model is constructed on Bit Diffusion (Chen et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib8)), where the architecture is U-Net (Ronneberger et al., [2015](https://arxiv.org/html/2410.22380v1#bib.bib46)) with 3 stages, 256 channels and 3 residual blocks

Table 4:Fid scores on Cifar-10.

|   |   |   |   |
|---|---|---|---|
|Models|Cifar-10 (Fid ⇓)|   |   |
|200K|500K|Final|
|Continuous Pixels|   |   |   |
|DDPM|-|-|3.17|
|DDIM|-|-|4.04|
|Discrete Ordinal Pixels|   |   |   |
|D3PM <br><br>Gauss|-|-|7.34|
|τLDR-0|-|-|8.10|
|τLDR-10|-|-|3.74|
|\hdashline   Binary Coding (uint8):|   |   |   |
|Bit Diffusion|-|-|3.48|
|Bit Diffusion <br><br>repro|22.12|13.23|10.37|
|Ours|8.17|5.03|3.86|
|\hdashline   Fixed Embedding:|   |   |   |
|Bit Diffusion <br><br>repro|19.69|16.61|12.96|
|Ours|12.32|10.09|9.15|
|Categorical Pixels|   |   |   |
|D3PM <br><br>Uniform|-|-|51.27|
|D3PM <br><br>Absorbing|-|-|30.97|
|\hdashline   Vector Quantization:|   |   |   |
|D3PM-VQ|-|-|16.47|
|τLDR-VQ|-|-|40.06|
|SDDM-VQ|-|-|12.23|
|\hdashline   Trainable Embedding:|   |   |   |
|Bit Diffusion <br><br>repro|33.09|27.21|19.26|
|Ours|21.17|15.32|10.99|

per stage. Diffusion steps are T=1000 for both the training and inference stages. The model is trained for 1.5⁢M steps with the learning rate of 1⁢e⁢4 and batch size of 128. Since the training script and detailed hyperparameters of Bit Diffusion are not available, we have to reproduce it by ourselves and our boundary conditional diffusion model shares exactly the same configuration. Our confidence factors are r=0.5 for all three settings. Other baselines include D3PM (Austin et al., [2021](https://arxiv.org/html/2410.22380v1#bib.bib3)) and τLDR (Campbell et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib5)) which are discrete diffusion models. SDDM (Sun et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib53)) utilizes vector quantization from VQGAN (Esser et al., [2021](https://arxiv.org/html/2410.22380v1#bib.bib11)) as a continuous space for discrete data. We also compare with DDPM (Ho et al., [2020](https://arxiv.org/html/2410.22380v1#bib.bib24)) and DDIM (Song et al., [2021a](https://arxiv.org/html/2410.22380v1#bib.bib51)) on continuous pixels.

![Refer to caption](https://arxiv.org/html/2410.22380v1/extracted/5961908/pics/bit.png)

(A)Bit Diffusion repro (Fid 10.37)

![Refer to caption](https://arxiv.org/html/2410.22380v1/extracted/5961908/pics/ddim.png)

(B)DDIM (Fid 4.04)

![Refer to caption](https://arxiv.org/html/2410.22380v1/extracted/5961908/pics/bit-rsa.png)

(C)Ours (Fid 3.86)

Figure 3:Generated images of Bit Diffusion 

repro

, DDIM, and Ours on Cifar-10.

#### Results

For binary coding, as shown in Table [5](https://arxiv.org/html/2410.22380v1#S5.SS0.SSS0.Px1 "Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), our approach outperforms the reproduced Bit Diffusion and attains competitive results to state-of-the-art models. For pixel embedding where ordinal information is deconstructed and reconstituted, our method exhibits a notable improvement of 3.81 Fid score over replicated Bit Diffusion. Moreover, in the case of categorical pixels, this advantage increases to 8.25, positioning our approach with trainable embedding as a new state-of-the-art solution. Additionally, as deterministic diffusion processes, our model with binary coding can slightly exceed the performance of DDIM, where the generated samples are in Figure [3](https://arxiv.org/html/2410.22380v1#S5.F3 "Figure 3 ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes").

#### Analysis

We analyze the influence of the confidence factor r in [Table 5](https://arxiv.org/html/2410.22380v1#S6.T5 "In 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"). The factor r is selected from [0,0.2,0.3,0.5], where r=0 is the reproduced Bit Diffusion that discards the discrete priors. As the confidence factor increases, the impact of discreteness gradually improves, simultaneously enhancing the model’s performance across all three settings. Since there is no guidance for unconditional image generation, we do not use a larger factor to prevent mode collapses.

## 6Related Work

Table 5:Confidence factors.

|Models|𝐫=𝟎|0.2|0.3|0.5|
|---|---|---|---|---|
|Binary Coding|10.37|7.39|5.33|3.86|
|Fixed Embedding|12.96|11.35|10.80|9.15|
|Trainable Embedding|19.26|15.32|11.56|10.99|

#### Discrete Modeling

Auto-regressive models have demonstrated a domination over discrete modeling, especially for text generation (Vaswani et al., [2017](https://arxiv.org/html/2410.22380v1#bib.bib56); Brown et al., [2020](https://arxiv.org/html/2410.22380v1#bib.bib4); Achiam et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib1)). However, the computation cost increases drastically as the size of sentence length or the image resolution increases. Diffusion models (Sohl-Dickstein et al., [2015](https://arxiv.org/html/2410.22380v1#bib.bib50); Ho et al., [2020](https://arxiv.org/html/2410.22380v1#bib.bib24); Dhariwal and Nichol, [2021](https://arxiv.org/html/2410.22380v1#bib.bib9); Saharia et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib48)) can generate data in parallel, but are tailored for continuous problems. To generalize diffusion models for discrete data, the most straightforward methods define discrete processes in discrete spaces (Sohl-Dickstein et al., [2015](https://arxiv.org/html/2410.22380v1#bib.bib50); Hoogeboom et al., [2021b](https://arxiv.org/html/2410.22380v1#bib.bib26); Austin et al., [2021](https://arxiv.org/html/2410.22380v1#bib.bib3); Campbell et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib5); Zhang et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib59); Sun et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib53); Lou et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib37)), which will be bothered by large number of discrete status. Besides, a simplified version of discrete diffusion processes is recently used in language modeling (He et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib21); Chen et al., [2023a](https://arxiv.org/html/2410.22380v1#bib.bib7)). Approaches in another line argue to located discrete data in continuous spaces, which is more flexible and efficient, with the mapping functions including binary bits (Chen et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib8)) and embeddings (Li et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib31); Gong et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib16), [a](https://arxiv.org/html/2410.22380v1#bib.bib15); Yuan et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib58); Gulrajani and Hashimoto, [2023](https://arxiv.org/html/2410.22380v1#bib.bib19); Han et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib20)). Other generative models adapted for discrete modeling includes Variational Autoencoders (Kingma and Welling, [2014](https://arxiv.org/html/2410.22380v1#bib.bib28)), Generative Adversarial Networks (Hjelm et al., [2018](https://arxiv.org/html/2410.22380v1#bib.bib23); Fedus et al., [2018](https://arxiv.org/html/2410.22380v1#bib.bib12)), and Normalizing Flows (Lindt and Hoogeboom, [2021](https://arxiv.org/html/2410.22380v1#bib.bib33); Hoogeboom et al., [2021a](https://arxiv.org/html/2410.22380v1#bib.bib25); Tan et al., [2022](https://arxiv.org/html/2410.22380v1#bib.bib55)).

#### Diffusion Models with Deterministic Trajectory

Deterministic diffusion process is usually used in the inference stage to speed up sampling, where DDIM (Song et al., [2021a](https://arxiv.org/html/2410.22380v1#bib.bib51)) derives a serial of non-Markovian diffusion processes and the deterministic one is a special case from this implicit perspective. Additionally, deterministic diffusion processes can be converted to ordinary differential equations (Song et al., [2021b](https://arxiv.org/html/2410.22380v1#bib.bib52)), which is utilized by recent sampling acceleration approaches such as DEIS (Zhang and Chen, [2023](https://arxiv.org/html/2410.22380v1#bib.bib60)) and DPM-Solvers (Lu et al., [2022b](https://arxiv.org/html/2410.22380v1#bib.bib39), [a](https://arxiv.org/html/2410.22380v1#bib.bib38); Zheng et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib61)). Our approach requires a deterministic forward trajectory to eliminate the randomness between the boundary point and sampled point. Flow matching (Liu, [2022](https://arxiv.org/html/2410.22380v1#bib.bib35); Lipman et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib34); Albergo and Vanden-Eijnden, [2023](https://arxiv.org/html/2410.22380v1#bib.bib2); Liu et al., [2023](https://arxiv.org/html/2410.22380v1#bib.bib36)) is a collection of generative models that employ ordinary differential equations to facilitate both forward and reverse processes. They can be regarded as generally equivalent to Diffusion models. Therefore, we extend the framework of flow matching for our method.

## 7Conclusion

We studied the gap between discrete modeling and continuous spaces, focusing on the inconsistency between probability density contours learned by continuous diffusion models and discrete boundaries. We have proposed a novel and general approach to address this issue by enabling continuous diffusion models to be conditioned on discrete priors, which is achieved via discrete boundary estimation and trajectory rescaling. An important limitation is that our method is designed for continuous diffusion models, where discrete diffusion models constructed specially on the discrete state space would not encounter the problem. However, discrete diffusion models also possess their own shortcomings, and the practical applications of continuous diffusion models are more extensive. We believe that our method has the potential to advance the development of unified and general diffusion models. By bridging the gap between discrete and continuous modeling, we hope to inspire new possibilities for modeling complex systems and phenomena.

## Acknowledgements

Bing Qin is the corresponding author of this work, We thank the anonymous reviewers for their insightful comments. This work was supported by the National Natural Science Foundation of China (NSFC) (U22B2059, grant 62276078), the Key R&D Program of Heilongjiang via grant 2022ZX01A32, the International Cooperation Project of PCL, PCL2022D01 and the Fundamental Research Funds for the Central Universities (Grant No.HIT.OCEF.2023018).

## References

- Achiam et al. [2023]Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al.Gpt-4 technical report._arXiv preprint arXiv:2303.08774_, 2023.
- Albergo and Vanden-Eijnden [2023]Michael Samuel Albergo and Eric Vanden-Eijnden.Building normalizing flows with stochastic interpolants.In _The Eleventh International Conference on Learning Representations_, 2023.URL [https://openreview.net/forum?id=li7qeBbCR1t](https://openreview.net/forum?id=li7qeBbCR1t).
- Austin et al. [2021]Jacob Austin, Daniel D. Johnson, Jonathan Ho, Daniel Tarlow, and Rianne van den Berg.Structured denoising diffusion models in discrete state-spaces.In A. Beygelzimer, Y. Dauphin, P. Liang, and J. Wortman Vaughan, editors, _Advances in Neural Information Processing Systems_, 2021.
- Brown et al. [2020]Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei.Language models are few-shot learners.In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin, editors, _Advances in Neural Information Processing Systems_, volume 33, pages 1877–1901. Curran Associates, Inc., 2020.
- Campbell et al. [2022]Andrew Campbell, Joe Benton, Valentin De Bortoli, Tom Rainforth, George Deligiannidis, and Arnaud Doucet.A continuous time framework for discrete denoising models.In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho, editors, _Advances in Neural Information Processing Systems_, 2022.
- Cettolo et al. [2012]Mauro Cettolo, Christian Girardi, and Marcello Federico.WIT3: Web inventory of transcribed and translated talks.In Mauro Cettolo, Marcello Federico, Lucia Specia, and Andy Way, editors, _Proceedings of the 16th Annual Conference of the European Association for Machine Translation_, pages 261–268, Trento, Italy, May 28–30 2012. European Association for Machine Translation.
- Chen et al. [2023a]Jiaao Chen, Aston Zhang, Mu Li, Alex Smola, and Diyi Yang.A cheaper and better diffusion language model with soft-masked noise.In Houda Bouamor, Juan Pino, and Kalika Bali, editors, _Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing_, pages 4765–4775, Singapore, December 2023a. Association for Computational Linguistics.
- Chen et al. [2023b]Ting Chen, Ruixiang Zhang, and Geoffrey Hinton.Analog bits: Generating discrete data using diffusion models with self-conditioning.In _The Eleventh International Conference on Learning Representations_, 2023b.
- Dhariwal and Nichol [2021]Prafulla Dhariwal and Alexander Nichol.Diffusion models beat gans on image synthesis.In M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and J. Wortman Vaughan, editors, _Advances in Neural Information Processing Systems_, volume 34, pages 8780–8794. Curran Associates, Inc., 2021.
- Dosovitskiy et al. [2021]Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil Houlsby.An image is worth 16x16 words: Transformers for image recognition at scale.In _International Conference on Learning Representations_, 2021.URL [https://openreview.net/forum?id=YicbFdNTTy](https://openreview.net/forum?id=YicbFdNTTy).
- Esser et al. [2021]Patrick Esser, Robin Rombach, and Bjorn Ommer.Taming transformers for high-resolution image synthesis.In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_, pages 12873–12883, 2021.
- Fedus et al. [2018]William Fedus, Ian Goodfellow, and Andrew M. Dai.Maskgan: Better text generation via filling in the _.In _International Conference on Learning Representations_, 2018.
- Gao et al. [2022]Zhujin Gao, Junliang Guo, Xu Tan, Yongxin Zhu, Fang Zhang, Jiang Bian, and Linli Xu.Difformer: Empowering diffusion model on embedding space for text generation._arXiv preprint arXiv:2212.09412_, 2022.
- Ghazvininejad et al. [2019]Marjan Ghazvininejad, Omer Levy, Yinhan Liu, and Luke Zettlemoyer.Mask-predict: Parallel decoding of conditional masked language models.In Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan, editors, _Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)_, pages 6112–6121, Hong Kong, China, November 2019. Association for Computational Linguistics.
- Gong et al. [2023a]Shansan Gong, Mukai Li, Jiangtao Feng, Zhiyong Wu, and Lingpeng Kong.DiffuSeq-v2: Bridging discrete and continuous text spaces for accelerated Seq2Seq diffusion models.In Houda Bouamor, Juan Pino, and Kalika Bali, editors, _Findings of the Association for Computational Linguistics: EMNLP 2023_, pages 9868–9875, Singapore, December 2023a. Association for Computational Linguistics.
- Gong et al. [2023b]Shansan Gong, Mukai Li, Jiangtao Feng, Zhiyong Wu, and Lingpeng Kong.Diffuseq: Sequence to sequence text generation with diffusion models.In _The Eleventh International Conference on Learning Representations_, 2023b.
- Gu et al. [2018]Jiatao Gu, James Bradbury, Caiming Xiong, Victor O.K. Li, and Richard Socher.Non-autoregressive neural machine translation.In _International Conference on Learning Representations_, 2018.
- Gu et al. [2019]Jiatao Gu, Changhan Wang, and Junbo Zhao.Levenshtein transformer.In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc, E. Fox, and R. Garnett, editors, _Advances in Neural Information Processing Systems_, volume 32. Curran Associates, Inc., 2019.
- Gulrajani and Hashimoto [2023]Ishaan Gulrajani and Tatsunori Hashimoto.Likelihood-based diffusion language models.In _Thirty-seventh Conference on Neural Information Processing Systems_, 2023.
- Han et al. [2023]Xiaochuang Han, Sachin Kumar, and Yulia Tsvetkov.SSD-LM: Semi-autoregressive simplex-based diffusion language model for text generation and modular control.In Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, editors, _Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, pages 11575–11596, Toronto, Canada, July 2023. Association for Computational Linguistics.
- He et al. [2023]Zhengfu He, Tianxiang Sun, Qiong Tang, Kuanning Wang, Xuanjing Huang, and Xipeng Qiu.DiffusionBERT: Improving generative masked language models with diffusion models.In Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, editors, _Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, pages 4521–4534, Toronto, Canada, July 2023. Association for Computational Linguistics.
- Heusel et al. [2017]Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter.Gans trained by a two time-scale update rule converge to a local nash equilibrium._Advances in neural information processing systems_, 30, 2017.
- Hjelm et al. [2018]R Devon Hjelm, Athul Paul Jacob, Adam Trischler, Gerry Che, Kyunghyun Cho, and Yoshua Bengio.Boundary seeking gans.In _International Conference on Learning Representations_, 2018.
- Ho et al. [2020]Jonathan Ho, Ajay Jain, and Pieter Abbeel.Denoising diffusion probabilistic models.In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin, editors, _Advances in Neural Information Processing Systems_, volume 33, pages 6840–6851. Curran Associates, Inc., 2020.
- Hoogeboom et al. [2021a]Emiel Hoogeboom, Didrik Nielsen, Priyank Jaini, Patrick Forré, and Max Welling.Argmax flows and multinomial diffusion: Learning categorical distributions.In M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and J. Wortman Vaughan, editors, _Advances in Neural Information Processing Systems_, volume 34, pages 12454–12465. Curran Associates, Inc., 2021a.
- Hoogeboom et al. [2021b]Emiel Hoogeboom, Didrik Nielsen, Priyank Jaini, Patrick Forré, and Max Welling.Argmax flows and multinomial diffusion: Learning categorical distributions.In A. Beygelzimer, Y. Dauphin, P. Liang, and J. Wortman Vaughan, editors, _Advances in Neural Information Processing Systems_, 2021b.
- Kim and Rush [2016]Yoon Kim and Alexander M. Rush.Sequence-level knowledge distillation.In Jian Su, Kevin Duh, and Xavier Carreras, editors, _Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing_, pages 1317–1327, Austin, Texas, November 2016. Association for Computational Linguistics.
- Kingma and Welling [2014]Diederik P. Kingma and Max Welling.Auto-encoding variational bayes.In _International Conference on Learning Representations_, 2014.
- Kong et al. [2021]Zhifeng Kong, Wei Ping, Jiaji Huang, Kexin Zhao, and Bryan Catanzaro.Diffwave: A versatile diffusion model for audio synthesis.In _International Conference on Learning Representations_, 2021.
- Krizhevsky et al. [2009]Alex Krizhevsky, Geoffrey Hinton, et al.Learning multiple layers of features from tiny images.2009.
- Li et al. [2022]Xiang Lisa Li, John Thickstun, Ishaan Gulrajani, Percy Liang, and Tatsunori Hashimoto.Diffusion-LM improves controllable text generation.In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho, editors, _Advances in Neural Information Processing Systems_, 2022.
- Lin [2004]Chin-Yew Lin.ROUGE: A package for automatic evaluation of summaries.In _Text Summarization Branches Out_, pages 74–81, Barcelona, Spain, July 2004. Association for Computational Linguistics.
- Lindt and Hoogeboom [2021]Alexandra Lindt and Emiel Hoogeboom.Discrete denoising flows.In _ICML Workshop on Invertible Neural Networks, Normalizing Flows, and Explicit Likelihood Models_, 2021.
- Lipman et al. [2023]Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, and Matthew Le.Flow matching for generative modeling.In _The Eleventh International Conference on Learning Representations_, 2023.
- Liu [2022]Qiang Liu.Rectified flow: A marginal preserving approach to optimal transport._arXiv preprint arXiv:2209.14577_, 2022.
- Liu et al. [2023]Xingchao Liu, Chengyue Gong, and Qiang Liu.Flow straight and fast: Learning to generate and transfer data with rectified flow.In _International conference on learning representations (ICLR)_, 2023.
- Lou et al. [2023]Aaron Lou, Chenlin Meng, and Stefano Ermon.Discrete diffusion language modeling by estimating the ratios of the data distribution._arXiv preprint arXiv:2310.16834_, 2023.
- Lu et al. [2022a]Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongxuan Li, and Jun Zhu.Dpm-solver++: Fast solver for guided sampling of diffusion probabilistic models._arXiv preprint arXiv:2211.01095_, 2022a.
- Lu et al. [2022b]Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongxuan Li, and Jun Zhu.DPM-solver: A fast ODE solver for diffusion probabilistic model sampling in around 10 steps.In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho, editors, _Advances in Neural Information Processing Systems_, 2022b.
- Madani et al. [2020]Ali Madani, Bryan McCann, Nikhil Naik, Nitish Shirish Keskar, Namrata Anand, Raphael R Eguchi, Po-Ssu Huang, and Richard Socher.Progen: Language modeling for protein generation._arXiv preprint arXiv:2004.03497_, 2020.
- Madani et al. [2023]Ali Madani, Ben Krause, Eric R Greene, Subu Subramanian, Benjamin P Mohr, James M Holton, Jose Luis Olmos, Caiming Xiong, Zachary Z Sun, Richard Socher, et al.Large language models generate functional protein sequences across diverse families._Nature Biotechnology_, 41(8):1099–1106, 2023.
- Ott et al. [2019]Myle Ott, Sergey Edunov, Alexei Baevski, Angela Fan, Sam Gross, Nathan Ng, David Grangier, and Michael Auli.fairseq: A fast, extensible toolkit for sequence modeling.In _Proceedings of NAACL-HLT 2019: Demonstrations_, 2019.
- Papineni et al. [2002]Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu.Bleu: a method for automatic evaluation of machine translation.In Pierre Isabelle, Eugene Charniak, and Dekang Lin, editors, _Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics_, pages 311–318, Philadelphia, Pennsylvania, USA, July 2002. Association for Computational Linguistics.
- Parmar et al. [2018]Niki J. Parmar, Ashish Vaswani, Jakob Uszkoreit, Lukasz Kaiser, Noam Shazeer, Alexander Ku, and Dustin Tran.Image transformer.In _International Conference on Machine Learning (ICML)_, 2018.URL [http://proceedings.mlr.press/v80/parmar18a.html](http://proceedings.mlr.press/v80/parmar18a.html).
- Rombach et al. [2022]Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer.High-resolution image synthesis with latent diffusion models.In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, pages 10684–10695, June 2022.
- Ronneberger et al. [2015]Olaf Ronneberger, Philipp Fischer, and Thomas Brox.U-net: Convolutional networks for biomedical image segmentation.In _Medical Image Computing and Computer-Assisted Intervention–MICCAI 2015: 18th International Conference, Munich, Germany, October 5-9, 2015, Proceedings, Part III 18_, pages 234–241. Springer, 2015.
- Rush et al. [2015]Alexander M. Rush, Sumit Chopra, and Jason Weston.A neural attention model for abstractive sentence summarization.In Lluís Màrquez, Chris Callison-Burch, and Jian Su, editors, _Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing_, pages 379–389, Lisbon, Portugal, September 2015. Association for Computational Linguistics.
- Saharia et al. [2022]Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, Jonathan Ho, David J Fleet, and Mohammad Norouzi.Photorealistic text-to-image diffusion models with deep language understanding.In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors, _Advances in Neural Information Processing Systems_, volume 35, pages 36479–36494. Curran Associates, Inc., 2022.
- Sennrich et al. [2016]Rico Sennrich, Barry Haddow, and Alexandra Birch.Neural machine translation of rare words with subword units.In Katrin Erk and Noah A. Smith, editors, _Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, pages 1715–1725, Berlin, Germany, August 2016. Association for Computational Linguistics.
- Sohl-Dickstein et al. [2015]Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli.Deep unsupervised learning using nonequilibrium thermodynamics.In Francis Bach and David Blei, editors, _Proceedings of the 32nd International Conference on Machine Learning_, volume 37 of _Proceedings of Machine Learning Research_, pages 2256–2265, Lille, France, 07–09 Jul 2015. PMLR.
- Song et al. [2021a]Jiaming Song, Chenlin Meng, and Stefano Ermon.Denoising diffusion implicit models.In _International Conference on Learning Representations_, 2021a.
- Song et al. [2021b]Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole.Score-based generative modeling through stochastic differential equations.In _International Conference on Learning Representations_, 2021b.
- Sun et al. [2023]Haoran Sun, Lijun Yu, Bo Dai, Dale Schuurmans, and Hanjun Dai.Score-based continuous-time discrete diffusion models.In _The Eleventh International Conference on Learning Representations_, 2023.
- Sutskever et al. [2014]Ilya Sutskever, Oriol Vinyals, and Quoc V Le.Sequence to sequence learning with neural networks._Advances in neural information processing systems_, 27, 2014.
- Tan et al. [2022]Shawn Tan, Chin-Wei Huang, Alessandro Sordoni, and Aaron Courville.Learning to dequantise with truncated flows.In _International Conference on Learning Representations_, 2022.
- Vaswani et al. [2017]Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia Polosukhin.Attention is all you need.In I. Guyon, U. Von Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, _Advances in Neural Information Processing Systems_, volume 30. Curran Associates, Inc., 2017.
- Ye et al. [2023]Jiasheng Ye, Zaixiang Zheng, Yu Bao, Lihua Qian, and Mingxuan Wang.Dinoiser: Diffused conditional sequence learning by manipulating noises._arXiv preprint arXiv:2302.10025_, 2023.
- Yuan et al. [2022]Hongyi Yuan, Zheng Yuan, Chuanqi Tan, Fei Huang, and Songfang Huang.Seqdiffuseq: Text diffusion with encoder-decoder transformers._ArXiv_, abs/2212.10325, 2022.
- Zhang et al. [2023]Pengze Zhang, Hubery Yin, Chen Li, and Xiaohua Xie.Formulating discrete probability flow through optimal transport.In _Thirty-seventh Conference on Neural Information Processing Systems_, 2023.
- Zhang and Chen [2023]Qinsheng Zhang and Yongxin Chen.Fast sampling of diffusion models with exponential integrator.In _The Eleventh International Conference on Learning Representations_, 2023.
- Zheng et al. [2023]Kaiwen Zheng, Cheng Lu, Jianfei Chen, and Jun Zhu.Dpm-solver-v3: Improved diffusion ode solver with empirical model statistics.In _Thirty-seventh Conference on Neural Information Processing Systems_, 2023.

## Appendix AStopping Time for Forward Process

The forward diffusion process 𝐗={𝐱n,n≥0} is a markovian stochastic process with a transition probability p⁢(𝐱i|𝐱i−1)=𝒩⁢(𝐱i;αi⁢𝐱i−1,(1−αi)⁢𝐈). And a stopping time t0 with respect to 𝐗 is a random time such that for each n≥0, the event {t0=n} is completely determined by the total information known up to time n, {𝐱0,…,𝐱n}. Suppose the random variables {𝐱n} are in a one-dimensional space and the forward process starts with 𝐱0=0. Besides, let A,𝐱0∈A be the discrete area belonging to 𝐱0 that for each points in area A will be regarded as 𝐱0 during data generation. Our expected stopping time is defined as: t_0=min{n≥0, x_n ∉A}, which represents the first time 𝐱n leaves area A. We can write the probability of stopping time as: P(t0=0) = P(x0∉A) = 0P(t0=1) = P(x0∈A, x1∉A)= ∫x1∉AN(x1;α1x0, (1-α1)  I)dx1P(t0=2) = P(x0∈A, x1∈A, x2∉A)= P(x0∈A, x1∈A) ×P(x2∉A | x1∈A) = ∫x2∉A[∫x1∈AN(x1;α1x0, (1-α1)  I)×N(x2;α2x1, (1-α2)  I)dx1]dx2⋯⋯P(t0=n) = P(x0∈A,…, xn-1∈A, xn∉A)= ∫xn∉A∫x≤n∈A∏i=1n-1N(xi;αixi-1, (1-αi)  I)dx1:n. Since the diffusion process is established in continuous space, calculating the probability of the stopping time requires integrating over each intermediate state 𝐱1:n−1, rather than a simple state transfer as in the discrete space. Hence, directly obtain the stopping time is intractable. Additionally, even if we are able to get probability of the stopping time, we can only get a distribution over the time dimension, without knowing the exact time of 𝐱n leaving area A. Therefore, we need to eliminate randomness from the state transition 𝐱i−1→𝐱i and find a deterministic forward trajectory to estimate the stopping time.

## Appendix BProperties of Dirac Delta Function

There are several useful properties of Dirac delta function:

- • 
    
    Symmetry Property: δ⁢(−x)=δ⁢(x)
    
- • 
    
    Scaling Property: δ⁢(a⁢x)=δ⁢(x)|a|
    
- • 
    
    Translation Property: ∫f⁢(x)⁢δ⁢(x−a)⁢dx=f⁢(a)
    

## Appendix CBridging Flow Matching and DDPM

In this work, we utilizes the framework of Flow Matching to model the diffusion processes, where the forward process is defined by flow functions in [eq. 5](https://arxiv.org/html/2410.22380v1#S3.E5 "In 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"). Although having different mathematical forms, it is essentially equivalent to traditional diffusion processes. Here, we provide an alternative form from the perspective of state transfer pt⁢(𝐱t|𝐱t−1).

### C.1Deterministic Forward Process

[Equation 5](https://arxiv.org/html/2410.22380v1#S3.E5 "In 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") gives the definition pt⁢(𝐱t|𝐱0)=[ψt]∗⁢π⁢(𝐱), where ψt⁢(𝐱)=𝐮t⁢𝐱0+𝐯t⁢𝐱. Here we provide the equivalent derivation of pt⁢(𝐱t|𝐱0) from the perspective of diffusion processes:

|   |   |   |   |   |
|---|---|---|---|---|
|||pt⁢(𝐱t\|𝐱0)=∫pt⁢(𝐱1:t\|𝐱0)⁢d𝐱1:t−1||(29)|
|||=∫p⁢(𝐱1\|𝐱0)⁢∏s=2tps⁢(𝐱s\|𝐱s−1,𝐱0)⁢d⁢𝐱1:t−1,||

where p⁢(𝐱1|𝐱0)=𝒩⁢(𝐮1⁢𝐱0,𝐯12⁢𝐈) is the first step of the forward process at which the global noise is introduced into the forward trajectory. The state transfer probability of forward process ps⁢(𝐱s|𝐱s−1,𝐱0)=δ⁢(𝐱s−𝐮s⁢𝐱0−𝐯s⁢ψs−11⁢(𝐱s−1)) is a Dirac delta function. Therefore,

|   |   |   |   |   |
|---|---|---|---|---|
|||pt⁢(𝐱t\|𝐱0)=∫∏s=3tps⁢(𝐱s\|𝐱s−1,𝐱0)⁢𝐝𝐱2:t−1||(30)|
|||×∫p2⁢(𝐱2\|𝐱1,𝐱0)⁢p⁢(𝐱1\|𝐱0)⁢d𝐱1⏟Q1,||

where we denote the integral of 𝐱1 as Q1. Based on

|   |   |   |   |   |
|---|---|---|---|---|
|||Q0=q⁢(𝐱1\|𝐱0)=𝒩⁢(𝐮1⁢𝐱0,𝐯12⁢𝐈)||(31)|
|||q2⁢(𝐱2\|𝐱1,𝐱0)=δ⁢(𝐱2−𝐮2⁢𝐱0−𝐯2⁢ψ11⁢(𝐱1))||
|||=δ⁢[𝐱2−𝐯2𝐯1⁢𝐱1−(𝐮2−𝐯2⁢𝐮1𝐯1)⁢𝐱0]||
|||=δ⁢[𝐱1−𝐯1𝐯2⁢𝐱2−(𝐮1−𝐯1⁢𝐮2𝐯2)⁢𝐱0]||
|||(Symmetry Property of Dirac Delta Function)||

and the Translation Property of the Dirac delta function, we can calculate Q1 as:

|   |   |   |   |   |
|---|---|---|---|---|
|||Q1=∫p2⁢(𝐱2\|𝐱1,𝐱0)⏟δ⁢(x−a)⁢p⁢(𝐱1\|𝐱0)⏟f⁢(x)⁢d𝐱1,||(32)|
|||where {x:𝐱1a:𝐯1𝐯2⁢𝐱2+(𝐮1−𝐯1⁢𝐮2𝐯2)⁢𝐱0||
|||⟹Q1=𝒩(𝐮2𝐱0,𝐯22𝐈.)||

Then we can continue the deviation of pt⁢(𝐱t|𝐱0) as:

|   |   |   |   |   |
|---|---|---|---|---|
||pt⁢(𝐱t\|𝐱0)|=∫Q0⁢∏s=2tps⁢(𝐱s\|𝐱s−1,𝐱0)⁢d⁢𝐱1:t−1||(33)|
|||=∫Q1⁢∏s=3tps⁢(𝐱s\|𝐱s−1,𝐱0)⁢d⁢𝐱2:t−1||
|||=⋯⁢⋯||
|||=∫pt⁢(𝐱t\|𝐱t−1)⁢Qt−2⁢d𝐱t−1||
|||=Qt−1=𝒩⁢(𝐮t⁢𝐱0,𝐯t2⁢𝐈)||

Therefore, the probability distribution of 𝐱t conditioned on 𝐱0 follows a Gaussian distribution 𝒩⁢(𝐮t⁢𝐱0,𝐯t2⁢𝐈), which is the same as in original DDPMs when the coefficient functions are defined as 𝐮t=α¯t and 𝐯t=1−α¯t. This provides an important benefit that the Flow Matching and diffusion models share the same training procedure.

### C.2Deterministic Reverse Process

The reverse tranfer probability follows Bayes’ rule:

|   |   |   |   |   |
|---|---|---|---|---|
|||p⁢(𝐱t−1\|𝐱t,𝐱0)=pt⁢(𝐱t\|𝐱t−1,𝐱0)⁢pt−1⁢(𝐱t−1\|𝐱0)pt⁢(𝐱t\|𝐱0)||(34)|
|||=pt−1⁢(𝐱t−1\|𝐱0)pt⁢(𝐱t\|𝐱0)×δ⁢[𝐱t−𝐯t𝐯t−1⁢𝐱t−1−(𝐮t−𝐯t⁢𝐮t−1𝐯t−1)⁢𝐱0].||

Since Dirac delta function has another form of

|   |   |   |   |
|---|---|---|---|
||δ(x)={+∞,x=00,x≠0,||(35)|

and pt⁢(𝐱t|𝐱0)>0, pt−1⁢(𝐱t−1|𝐱t)>0, we have

|   |   |   |   |   |
|---|---|---|---|---|
||p⁢(𝐱t−1\|𝐱t,𝐱0)|=pt⁢(𝐱t\|𝐱t−1,𝐱0)⁢pt−1⁢(𝐱t−1\|𝐱0)pt⁢(𝐱t\|𝐱0)||(36)|
|||={+∞×pt−1⁢(𝐱t−1\|𝐱0)pt⁢(𝐱t\|𝐱0)⏞>0,𝐱t=[𝐯t𝐯t−1⁢𝐱t−1+(𝐮t−𝐯t⁢𝐮t−1𝐯t−1)⁢𝐱0]0,𝐱t≠[𝐯t𝐯t−1⁢𝐱t−1+(𝐮t−𝐯t⁢𝐮t−1𝐯t−1)⁢𝐱0]||
|||≃{+∞,𝐱t−1=[𝐯t−1𝐯t⁢𝐱t+(𝐮t−1−𝐮t⁢𝐯t−1𝐯t)⁢𝐱0]0,𝐱t−1≠[𝐯t−1𝐯t⁢𝐱t+(𝐮t−1−𝐮t⁢𝐯t−1𝐯t)⁢𝐱0]||
|||=δ⁢[𝐱t−1−𝐯t−1𝐯t⁢𝐱t−(𝐮t−1−𝐮t⁢𝐯t−1𝐯t)⁢𝐱0]||
|||=limσ→0𝒩⁢(𝐯t−1𝐯t⁢𝐱t+(𝐮t−1−𝐮t⁢𝐯t−1𝐯t)⁢𝐱0,σ2⁢𝐈).||

### C.3Deterministic Optimization Objective

We first include the derivation of the variational bound for diffusion models provided by Sohl-Dickstein et al. [[2015](https://arxiv.org/html/2410.22380v1#bib.bib50)]. The probability the generative model assigns to the data is:

|   |   |   |   |   |
|---|---|---|---|---|
||p⁢(𝐱0)|=∫p⁢(𝐱0:T)⁢d𝐱1:T||(37)|
|||=∫p⁢(𝐱0:T)⁢pT⁢(𝐱1:T\|𝐱0)pT⁢(𝐱1:T\|𝐱0)⁢d𝐱1:T||
|||=∫pT⁢(𝐱1:T\|𝐱0)⁢p⁢(𝐱0:T)pT⁢(𝐱1:T\|𝐱0)⁢d𝐱1:T||
|||=∫pT⁢(𝐱1:T\|𝐱0)⁢p⁢(𝐱T)⁢∏t=1Tp⁢(𝐱t−1\|𝐱t)pt⁢(𝐱t\|𝐱t−1)⁢d⁢𝐱1:T.||

Training amounts to minimizing the negative log likelihood:

|   |   |   |   |
|---|---|---|---|
||ℒ|=−∫p⁢(𝐱0)⁢log⁡p⁢(𝐱0)⁢d𝐱0||
|||=−∫p⁢(𝐱0)⁢log⁡[∫pT⁢(𝐱1:T\|𝐱0)⁢p⁢(𝐱T)⁢∏t=1Tp⁢(𝐱t−1\|𝐱t)pt⁢(𝐱t\|𝐱t−1)⁢d⁢𝐱1:T]⁢d𝐱0||
|||≤−∫pT⁢(𝐱0:T)⁢log⁡[p⁢(𝐱T)⁢∏t=1Tp⁢(𝐱t−1\|𝐱t)pt⁢(𝐱t\|𝐱t−1)]⁢d𝐱0:T||
|||=𝔼pT⁢(𝐱0:T)⁢[−log⁡p⁢(𝐱T)+∑t=1Tlog⁡pt⁢(𝐱t\|𝐱t−1)p⁢(𝐱t−1\|𝐱t)]||
|||=𝔼pT⁢[log⁡pT⁢(𝐱T\|𝐱0)p⁢(𝐱T)−log⁡p⁢(𝐱0\|𝐱1)+∑t=2Tlog⁡p⁢(𝐱t−1\|𝐱t,𝐱0)p⁢(𝐱t−1\|𝐱t)]||
|||=𝔼pT⁢[DKL(pT(𝐱T\|𝐱0)\|p(𝐱T))⏟ℒT⁢−log⁡p⁢(𝐱0\|𝐱1)⏟ℒ0+∑t=2TDKL(p(𝐱t−1\|𝐱t,𝐱0)\|p(𝐱t−1\|𝐱t))⏟ℒt−1]||

where ℒT is usually ignored as a constant and p⁢(𝐱t−1|𝐱t) is parameterized with a neural network pθ⁢(𝐱t−1|𝐱t) to approximate the conditioned probability distributions in the reverse process. Since p⁢(𝐱t−1|𝐱t,𝐱0)=limσ→0𝒩⁢(𝐯t−1𝐯t⁢𝐱t+(𝐮t−1−𝐮t⁢𝐯t−1𝐯t⁢𝐱0),σ2⁢𝐈), the parameterized pθ⁢(𝐱t−1|𝐱t) can take the same form 𝒩⁢(𝝁θ⁢(𝐱t,t),σt2⁢𝐈) because the Dirac delta function is a special case of Gaussian distribution and the KL divergence of two Gaussians can be simplified. Finally, the training objective for the deterministic diffusion process is divided as:

|   |   |   |   |
|---|---|---|---|
||ℒ={ℒT:a constantℒ0:−log⁡δ⁢(𝐱0−𝐱θ⁢(𝐱1,1))ℒt−1:c⁢∥𝐱0−𝐱θ⁢(𝐱t,t)∥2+limσ→0log⁡σtσc=12⁢σt2⁢(𝐮t−1−𝐮t⁢𝐯t−1𝐯t−1)2,||(38)|

where the simplified version ∥𝐱0−𝐱θ⁢(𝐱t,t)∥2 is the same as DDPMs but with different coefficients.

## Appendix DDifferent Diffusion Trajectories

![Refer to caption](https://arxiv.org/html/2410.22380v1/x3.png)

Figure 4:We demonstrate the trajectory differences among Markovian Diffusion Process, Deterministic Diffusion and Flow Matching.

We illustrate the trajectories of different diffusion processes in Figure [4](https://arxiv.org/html/2410.22380v1#A4.F4 "Figure 4 ‣ Appendix D Different Diffusion Trajectories ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"). The forward and reverse generation for the Markovian diffusion process is:

|   |   |   |   |
|---|---|---|---|
||{𝐱t=α¯t⁢𝐱0+1−α¯t⁢ϵt𝐱t−1=α¯t−1⁢(1−αt)1−α¯t⁢𝐱0+αt⁢(1−α¯t−1)1−α¯t⁢𝐱t+(1−α¯t−1)⁢(1−αt)1−α¯t⁢ϵt−1.||(39)|

The deterministic diffusion process:

|   |   |   |   |
|---|---|---|---|
||{𝐱t=α¯t⁢𝐱0+1−α¯t⁢ϵ𝐱t−1=(α¯t−1−α¯t⁢(1−α¯t−1)1−α¯t)⁢𝐱0+1−α¯t−11−α¯t⁢𝐱t.||(40)|

The deterministic flow matching with optimal transport:

|   |   |   |   |
|---|---|---|---|
||{𝐱t=(1−tT)⁢𝐱0+tT⁢ϵ𝐱t−1=1t⁢𝐱0+t−1t⁢𝐱t.||(41)|

## Appendix EDetails of the Function G

[Equation 13](https://arxiv.org/html/2410.22380v1#S3.E13 "In Flow Matching ‣ 3.1 Estimate Discrete Boundaries ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") defines the function G⁢(𝐱,ϵ) as the inversion of coefficient function.

#### Flow Matching

The coefficient is 𝐮t=1−t/T, where t=T×(1−𝐮t). Therefore,

|   |   |   |   |
|---|---|---|---|
||G⁢(𝐱0,ϵ)=t0=T×(1−𝐮t0)=T/(1+f⁢(ϵ,𝒥)−f⁢(ϵ,ℐ)f⁢(𝐱0,ℐ)−f⁢(𝐱0,𝒥))||(42)|

#### Diffusion

The coefficient for Variance Exploding is 𝐯T=σ0⁢(σTσ0)tT, where t=T×log⁡𝐯t−log⁡σ0log⁡σT−log⁡σ0.

|   |   |   |   |
|---|---|---|---|
||G⁢(𝐱0,ϵ)=t0=𝐯t0=T×log⁡𝐯t−log⁡σ0log⁡σT−log⁡σ0=T×log⁡f⁢(ϵ,𝒥)−f⁢(ϵ,ℐ)f⁢(𝐱0,ℐ)−f⁢(𝐱0,𝒥)−log⁡σ0log⁡σT−log⁡σ0.||(43)|

For Variance Preserving, the function G⁢(𝐱0,ϵ) is more difficult to calculate since 𝐮t=α¯t, where α¯=∏i=1tαi, αt=1−βt, and βt is also influenced by noise schedulers. This makes G⁢(𝐱0,ϵ) hard to calculate. Fortunately, we can bypass this function and provide the corresponding pseudo code.

## Appendix FDetails of the Training Objective

The rescaled vector field is calculated as:

|   |   |   |   |   |
|---|---|---|---|---|
||u~t|=d⁢𝐱~td⁢t=d⁢𝐱~td⁢τ⁢d⁢τd⁢t||(44)|
|||=[𝐮′⁢(𝐱0,τ)⁢𝐱0+𝐯′⁢(𝐱0,τ)⁢ϵ]⁢T−r×G⁢(𝐱0,ϵ)T||
|||=uτ×T−r×G⁢(𝐱0,ϵ)T.||

Considering the expectation form of u~t, there is:

|   |   |   |   |   |
|---|---|---|---|---|
||𝔼𝐱~t⁢[u~t⁢(𝐱~t\|𝐱0)]|=∑p⁢(𝐱~t\|𝐱0)⁢u~t⁢(𝐱~t\|𝐱0)||(45)|
|||=∑p⁢(𝐱~t\|𝐱0)⁢[𝐮′⁢(𝐱0,τ)⁢𝐱0+𝐯′⁢(𝐱0,τ)⁢ϵ]⁢T−r×G⁢(𝐱0,ϵ)T⏟0≤coefficient≤1||
|||≤∑p⁢(𝐱~t\|𝐱0)⁢[𝐮′⁢(𝐱0,τ)⁢𝐱0+𝐯′⁢(𝐱0,τ)⁢ϵ]||
|||=𝐮′⁢(𝐱0,τ)⁢[∑p⁢(𝐱~t\|𝐱0)⁢𝐱0]+𝐯′⁢(𝐱0,τ)⁢ϵ||
|||=u~t⁢(𝐱~0\|𝔼𝐱~t⁢[𝐱0]).||

Therefore, the training objective 𝔼⁢∥u~t−u~θ∥2≤c⁢𝔼⁢∥𝐱0−𝐱θ∥2, where c is the coefficient.

## Appendix GCode Implementations

Our framework is a module constructed on current diffusion models. We demonstrate our kernel part rescale diffusion trajectory with pseudo python code as below:

labels, alphas_cumprod, timesteps, mode):

#embedding: embedding matrix, f(x,i)=(embedding * x)[i]

#labels: I

#alphas_cumprod: list of all u_t

#timesteps: t

#mode: noising or denoising

#1. get f(x,i):

self_dot = torch.sum(embedding * embedding, dim=-1)

f_x_i = self_dot[labels][…, None]

labels = labels[…, None]

#2. get f(x,j) and f(eps,j):

embedding = embedding.permute(1, 0)

f_x_j = torch.matmul(x_0, embedding)

f_eps_j = torch.matmul(epsilon, embedding)

#3. get f(x,i) - f(x,j): (usually >=0; smaller -> closer)

#filter out f(x,i)-f(x,i) with a large positive number 100

fxi_minus_fxj = (f_x_i - f_x_j).scatter(-1, labels, 100)

#4. get f(eps,i) and f(eps,j) - f(eps,i): (larger -> more noise)

f_eps_i = torch.gather(f_eps_j, -1, labels)

#filter out f(eps,i)-f(eps,i) with a large negative number -100

fepsj_minus_fepsi = (f_eps_j - f_eps_i).scatter(-1, labels, -100)

#5. get fraction and u_t_0

#mask results outside the support set

info_mask = (fepsj_minus_fepsi < 0) | (fxi_minus_fxj < 0)

fraction = fix_minus_fjx / fjeps_minus_fieps

fraction[info_mask] = 100

min_frac, _ = fraction.min(dim=-1) # minimum

#Diffusion Variance Preserving eq. (9)

u_t_0 = torch.sqrt(1 / (1 + min_frac ** 2))[…, None]

#6. rescale timesteps

sqrt_alphas_cumprod = torch.sqrt(alphas_cumprod)

###!!!important trick!!!###

#We do not need to calculate the function G(x_0,t) (eq. (12)).

#Timesteps of diffusion processes are discrete and

# we just iterate over and compare with all coefficient functions.

#Besides, function G is easy to calculate for Flow Matching.

index = torch.sum(u_t_0 < sqrt_alphas_cumprod, dim=-1)

#T is the maximum timestep, for example T=2000.

#confactor is the confidency factor

#tau is the rescaled timestep

#delta_tau is the rescaled decoding velocity

if mode == ’noising’:

tau = (timesteps + index - \

(((timesteps + 1) / T) * index)).long().clamp(0, T)

tau = (confactor * tau.float() + \

(1.0 - confactor) * timesteps.float()).long().clamp(0, T)

return tau

elif mode == ’denoising’:

delta_tau = (T - index) / T

delta_tau = (confactor * delta_tau + \

(1 - confactor) * 1.0).clamp(0, 1)

return delta_tau

## Appendix HAnalysis

Table 6:Fid of difference sampling strategies.

||Gaussian|Deterministic|
|---|---|---|
|Binary Coding|13.39|3.86|
|Fixed Embedding|12.21|9.15|
|Trainable Embedding|22.24|10.99|

Algorithm 3 Gaussian Sampling

1:  t≔T, τ≔T

2:  𝐱~t∼𝒩⁢(𝟎,𝐈)// Initialing

3:  for Δ⁢t≔Δ⁢t1,…,Δ⁢ts do // ∑Δ⁢t=T

4:     𝐳∼𝒩⁢(𝟎,σt2⁢𝐈)// Gaussian Noise

5:     𝐱^0≔𝐱θ⁢(𝐱~t,t)// Pseudo Target

6:     ϵ^≔Ψ1⁢([𝐱~t;τ])// Trajectory Alteration

7:     τΔ≔𝒯⁢(t−Δ⁢t,G⁢(𝐱^0,ϵ^))// [eq. 25](https://arxiv.org/html/2410.22380v1#S3.E25 "In Reverse Process ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes")

8:     𝐱~t≔𝐮⁢(𝐱^0,τΔ)⁢𝐱^0+𝐯⁢(𝐱^0,τΔ)⁢ϵ^+𝐳

9:     t≔t−Δ⁢t, τ≔τΔ// Updating

10:  end for

11:  𝐱0≔𝐱θ⁢(𝐱~t,t)// 𝐱1→𝐱0

12:  return 𝐱0

#### Gaussian Sampling

Our framework is compatible with the Gaussian sampling in DDPM, where random noises can be added into each iteration step. [Algorithm 3](https://arxiv.org/html/2410.22380v1#alg3 "In Appendix H Analysis ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") demonstrates the Gaussian sampling procedure. Compared with [algorithm 2](https://arxiv.org/html/2410.22380v1#alg2 "In Reverse Process ‣ 3.3 Recover Data from Noise ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), a Gaussian noise 𝐳∼𝒩⁢(𝟎,σt2⁢𝐈) with a decreasing variance σt is injected to the estimated next state 𝐱~t. This noise 𝐳 will be mapped as changing the initial sampling 𝐱~T through the trajectory alteration step. We illustrate the deterministic and Gaussian sampling for our model on Cifar-10 in Table [6](https://arxiv.org/html/2410.22380v1#A8.T6 "Table 6 ‣ Appendix H Analysis ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), where the deterministic sampling can achieve a much better performance of Fid. We assume this is because our coefficient functions 𝐮⁢(𝐱0,t) and 𝐯⁢(𝐱0,t) are dynamically calculated to rescale the deterministic trajectory in the training stage. In the inference stage, 𝐱0 is replaced by 𝐱θ⁢(𝐱t,t), where errors will accumulate if the predicted pseudo target changes frequently. Moreover, Gaussian sampling will further introduce random noises at each reverse step, making our rescaled timestep τ far away from the training situation. Therefore, errors in the calculations of trajectory scaling will explode over iterations.

## Appendix ILimitations

Our framework is proposed to migrate the powerful continuous diffusion models to discrete problems. There is another technical route that directly designs the diffusion process on the discrete state space and our method is not useful for this scenario. However, we believe the continuous diffusion models can be a general framework for generative modeling and our effort can advance this target.

We prefer 𝐱0 as the training target because we highly depend on the reliability of the predicted 𝐱^0 during inference. Although it is possible to use other targets, the modeling effect will decrease in practical use, which limits the flexibility of diffusion modeling. For example, predicting the ϵ^ and recovering 𝐱^0 with [eq. 23](https://arxiv.org/html/2410.22380v1#S3.E23 "In 3.2 Rescale the Forward Trajectory ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") is inefficient, because a small error in predicting ϵ^ will be amplified by [eq. 23](https://arxiv.org/html/2410.22380v1#S3.E23 "In 3.2 Rescale the Forward Trajectory ‣ 3 Methodology ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and lead to the collapse of G⁢(𝐱^0,ϵ^).

Our approach requires extra computational cost. But they are acceptable since our rescaling process is a series of parallel matrix computations. Considering that our approach is compatible with the Self-Conditioning [Chen et al., [2023b](https://arxiv.org/html/2410.22380v1#bib.bib8)], our overhead is negligible when it is used.

## Appendix JOther Experimental Details

For language modeling, we utilize the model configuration transformer-iwslt-de-en in Fairseq framework [Ott et al., [2019](https://arxiv.org/html/2410.22380v1#bib.bib42)] for Iwslt14 de-en, which has 6 transformer layers, 4 attention heads, 512 hidden dimensions, and 1024 feed forward layer dimensions. For other datasets, the configuration is transformer-base, which has 6 transformer layers, 8 attention heads, 512 hidden dimensions, and 2048 feed forward layer dimensions. The embedding dimension is 128. The beam size is 1 length prediction beam × 5 generation beam, since the length prediction is unstable for diffusion language models. For reranking, we take 7 length prediction beam × 3 generation beam as Difformer to let the transformer choose the best one.

For image generation, we set the scaling factor r=0.5 for training. Besides, we find that a smaller factor for inference is sometime useful. We set r=0.45 on binary coding and r=0.2 on fixed embedding during inference. When the pixel embedding is learnable, the scaling factor is r=0.5, which is the same as training.

Our experiments are performed with Nvidia 80G A100. Each language result requires about 2 days on one single A100. Each image result requires about a week on one single A100.

## Appendix KImpact Statements

This paper presents work whose goal is to advance the field of Deep Learning. The datasets we used has been widely deployed for many years and has basically no negative impact. Our approach is a framework that migrates existing diffusion models to discrete problems, which does not provide a large pre-trained model that can be used to generate fake contents.

## Appendix LCase Study

Table 7:Cases of translation on Iwslt14 de-en.

|Source: German|Target: English|   |   |
|---|---|---|---|
||Difformer|Ours|Golden|
|---|---|---|---|
|ich möchte ihnen erzählen , wie wir das herausgefunden haben .|i want to tell you about this .|i want to tell you how we ’ ve figured that out .|i want to tell you how we found that out .|
|da gingen ganz schön viele verrückte dinge vor sich .|lots of crazy things .|there were quite a lot of crazy things going on .|there was a whole lot of crazy going on in there .|
|man macht etwas , das eigentlich ein wenig anders ist .|you do something a little different .|you ’ re doing something that ’ s actually a little bit different .|you do something that ’ s actually a little different .|
|und die welt in der wir lebten sah so aus .|and the world we lived like this .|and the world we lived in looked like this .|and the world we used to live in looked like this .|
|man erwartet eine zusätzliche milliarde spieler im nächsten jahrzehnt .|you ’ ll expect an next billion players .|you expect an extra billion players in the next decade .|they expect one billion more gamers in the next decade .|
|b hat diese vorteile und risiken . was wollen sie tun ?|b has risks . what do you want to do ?|b has these benefits and risks . what do you want to do ?|b has these benefits , and these risks . what do you want to do ?|
|wir haben also so eine situation , wo , je weiter unsere wissenschaft fortschreitet , wir uns um so mehr eingestehen müssen , dass diese kategorien , die wir für stabile anatomische kategorien gehalten hatten , welche sehr einfache zuordnungen herstellten um dauerhafte identitätskategorien zu schaffen , viel unschärfer sind , als wir angenommen haben .|so we have this situation where the continuing our science continues , we need to admit the more that these categories that we thought were stable anatomical categories , which made a very simple collaborations to create permanent identity ories are much unsharers than we ’ ve assumed .|so we have a situation where , as the further our science goes on , we have to admit in terms , the more that these categories that we thought of be a stable anatomical categories , which made a very simple assaments to create permanent identity categories , are much more blanky than we ’ ve accepted .|so what we have is a sort of situation where the farther our science goes , the more we have to admit to ourselves that these categories that we thought of as stable anatomical categories that mapped very simply to stable identity categories are a lot more fuzzy than we thought .|

Table 8:Cases of summarization on Gigaword.

|Source|Target|   |   |
|---|---|---|---|
||Difformer|Ours|Golden|
|---|---|---|---|
|the asian swimming record tumbled again at the seven-day olympic test event here on friday .|asian swimming record falls again|asian swimming tumble again at olympic test event|asian swimming record tumbles again at china ’s olympic trials|
|a truck carrying illegal north african immigrants flipped over in northeastern spain , killing ## and injuring six others , police said monday .|truck carrying illegal immigrants crashes in spain killing ##|## illegal immigrants killed in truck accident in northeastern spain|## immigrants killed in road accident in spain|
|new zealand share prices closed #.## percent lower wednesday after investors took their lead from further weakness in overseas markets , dealers said .|new zealand shares fall #.## percent|new zealand shares close #.## percent lower|new zealand shares close down #.## percent|
|the sudanese opposition said here thursday it had killed more than ### government soldiers in an ambush in the east of the country .|sudanese opposition claims over ### soldiers killed|sudanese opposition claims ### soldiers killed in ambush|sudanese opposition says ### government troops killed in ambush|
|these sports stories for release tuesday , september ## , #### , are moving today to clients of the new york times news service .|thursday ’s sports budget|cox news service sports budget|cox news service tuesday sports budget|
|bangladesh and india signed a deal here thursday giving green signal to resumption of passenger train service between the two neighboring countries after ## years .|bangladesh india sign agreement on train service|bangladesh india sign agreement to resume train service|bangladesh india sign agreement for resumption of train service after ## years|

Generated sentences on Iwslt14 de-en and Gigaword are illustrated in Table [7](https://arxiv.org/html/2410.22380v1#A12.T7 "Table 7 ‣ Appendix L Case Study ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes") and Table [8](https://arxiv.org/html/2410.22380v1#A12.T8 "Table 8 ‣ Appendix L Case Study ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"). Generated images on Cifar-10 are depicted in Figure [5](https://arxiv.org/html/2410.22380v1#A12.F5 "Figure 5 ‣ Appendix L Case Study ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), [6](https://arxiv.org/html/2410.22380v1#A12.F6 "Figure 6 ‣ Appendix L Case Study ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes"), and [7](https://arxiv.org/html/2410.22380v1#A12.F7 "Figure 7 ‣ Appendix L Case Study ‣ Acknowledgements ‣ 7 Conclusion ‣ Diffusion Models with Deterministic Trajectory ‣ 6 Related Work ‣ Analysis ‣ Results ‣ Experimental Setup ‣ 5 Discrete Image Generation ‣ Discrete Modeling via Boundary Conditional Diffusion Processes").

![Refer to caption](https://arxiv.org/html/2410.22380v1/extracted/5961908/pics/bit.png)

(A)Bit Diffusion repro (Fid 10.37)

![Refer to caption](https://arxiv.org/html/2410.22380v1/extracted/5961908/pics/bit-rsa.png)

(B)Ours (Fid 3.86)

Figure 5:Generated Binary Coding images of reproduced Bit Diffusion and Ours on Cifar-10.

![Refer to caption](https://arxiv.org/html/2410.22380v1/extracted/5961908/pics/embit.png)

(A)Bit Diffusion repro (Fid 12.96)

![Refer to caption](https://arxiv.org/html/2410.22380v1/extracted/5961908/pics/embit-rsa.png)

(B)Ours (Fid 9.15)

Figure 6:Generated Fixed Embedding images of reproduced Bit Diffusion and Ours on Cifar-10.

![Refer to caption](https://arxiv.org/html/2410.22380v1/extracted/5961908/pics/emb.png)

(A)Bit Diffusion repro (Fid 19.26)

![Refer to caption](https://arxiv.org/html/2410.22380v1/extracted/5961908/pics/emb-rsa.png)

(B)Ours (Fid 10.99)

Figure 7:Generated Trainable Embedding images of reproduced Bit Diffusion and Ours on Cifar-10.