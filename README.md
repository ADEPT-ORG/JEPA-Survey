# JEPA-Survey: A Paper List on Joint-Embedding Predictive Architectures

A curated list of papers on **Joint-Embedding Predictive Architectures (JEPA)** and JEPA-based world models, organized by the taxonomy of our survey: static/foundational (JEPA-F), temporal (JEPA-T), action-conditioned (JEPA-A), multimodal (JEPA-M), and structured/scene-centric (JEPA-SC) methods, followed by application domains.

This repository accompanies our survey on JEPA and world models. The paper link will be added here once it is public.

**1085 papers** in total: 632 JEPA papers, 298 related works that use, evaluate or discuss JEPA, and 155 background references cited in the survey. Last updated: 2026-11-21.

If a paper is missing or an entry is wrong, pull requests and issues are welcome.

## How this list is built

- **Sources.** arXiv records whose title or abstract mentions JEPA (or a JEPA-derived name such as LeJEPA or LeWorldModel), non-arXiv papers with JEPA in the title indexed by OpenAlex, and the reference list of the survey.
- **Venue.** Taken from the arXiv journal reference or comment field and from Semantic Scholar. Papers without a confirmed venue are listed as `arXiv`.
- **Code/Project.** The link the authors give in the arXiv abstract or comments. `-` means no link was found automatically, not that no code exists.
- **Categories.** Assigned by keyword rules with a manual pass over part of the list. The JEPA-F/T/A/M/SC labels of the methods analyzed in the survey follow the paper.

The venue, code and category fields are extracted automatically and will contain errors. Corrections are welcome. The scripts are in [`tools/`](tools) and the data in [`data/papers.json`](data/papers.json).

## Contents

- [JEPA Methods](#jepa-methods)
  - [Surveys and Tutorials](#surveys-and-tutorials) (4)
  - [Theory and Analysis](#theory-and-analysis) (39)
  - [JEPA-F: Image and Static Representation Learning](#jepa-f-image-and-static-representation-learning) (47)
  - [JEPA-T: Video and Temporal Prediction](#jepa-t-video-and-temporal-prediction) (51)
  - [JEPA-A: Action-Conditioned World Models, Planning and Control](#jepa-a-action-conditioned-world-models-planning-and-control) (171)
  - [JEPA-M: Multimodal](#jepa-m-multimodal) (24)
  - [JEPA-SC: 3D, Structured and Object-Centric](#jepa-sc-3d-structured-and-object-centric) (24)
- [Applications](#applications)
  - [Autonomous Driving](#autonomous-driving) (24)
  - [Medical and Healthcare](#medical-and-healthcare) (78)
  - [Scientific Domains](#scientific-domains) (43)
  - [Remote Sensing](#remote-sensing) (18)
  - [Audio, Speech and Music](#audio-speech-and-music) (21)
  - [Language and Reasoning](#language-and-reasoning) (16)
  - [Time Series, Tabular and Trajectories](#time-series-tabular-and-trajectories) (32)
  - [Graphs and Recommendation](#graphs-and-recommendation) (17)
  - [Wireless, Networks and Security](#wireless-networks-and-security) (19)
  - [Other](#other) (4)
- [Related Work That Uses, Evaluates or Discusses JEPA](#related-work-that-uses-evaluates-or-discusses-jepa) (298)
- [Background Cited in the Survey](#background-cited-in-the-survey) (155)

## JEPA Methods

### Surveys and Tutorials

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | Advanced Engineering Informatics | - | [Joint Embedding Predictive Architecture for autonomous vehicle safety and security: A comprehensive survey](https://doi.org/10.1016/j.aei.2026.104598) | - |
| 2026 | Neurocomputing | - | [Predicting representations, modeling worlds, recovering causes: A critical review of JEPA, world models, and causal representation learning](https://doi.org/10.1016/j.neucom.2026.135279) | - |
| 2025 | SSRN | - | [A Survey on Joint Embedding Predictive Architectures and World Models](https://doi.org/10.2139/ssrn.5772122) | - |
| 2025 | OpenReview | - | [Tutorial on Joint Embedding Predictive Architectures (JEPA): Foundations, Applications, and Future Directions](https://openreview.net/forum?id=Zr4PUe0ZNl) | - |

### Theory and Analysis

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [$λ$-JEPA Spectral Anti-Collapse Regularization for Self-Supervised Learning](https://arxiv.org/abs/2609.35288) | [Code](https://github.com/berkerdemirel/lambda-jepa) |
| 2026 | arXiv | - | [A Generalization Theory for JEPA-Based World Models](https://arxiv.org/abs/2606.27014) | - |
| 2026 | arXiv | - | [A Stochastic Latent Variable Generalization of Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2611.09302) | - |
| 2026 | arXiv | - | [Beyond Gaussian Worlds: Latent Geometry Matters for JEPAs](https://arxiv.org/abs/2609.21656) | - |
| 2026 | arXiv | - | [Beyond Isotropy in JEPAs: Hamiltonian Geometry and Symplectic Prediction](https://arxiv.org/abs/2605.20107) | - |
| 2026 | International Symposium on Smart Systems | CI-JEPA | [CI-JEPA: A Counterfactual Analysis of Latent Representations in Joint-Embedding Predictive Architectures for Self-Supervised Learning](https://arxiv.org/abs/2610.05043) | - |
| 2026 | TMLR | - | [Contractive MASO‑Generalized Predictors for Stable Latent‑Space Learning in JEPA](https://openreview.net/forum?id=k2Z2gPOtlq) | - |
| 2026 | arXiv | CSWAM | [CSWAM: Better Causal Semantic Representations for Out-of-Distribution Generalization in World Action Models](https://arxiv.org/abs/2609.18462) | - |
| 2026 | arXiv | DSReg | [DSReg: Provably Recovering Individual World Latents without Reconstruction](https://arxiv.org/abs/2610.09457) | [Project](https://dsreg.github.io/) |
| 2026 | Preprints.org | Dynamic LeJEPA | [Dynamic LeJEPA: Maximum Entropy Representations for Sequential Prediction and Latent Planning with Theoretical Guarantees](https://doi.org/10.20944/preprints202609.0981.v1) | - |
| 2026 | arXiv | Expanding SPHERE-JEPA | [Expanding SPHERE-JEPA: A Family of Statistical Regularizers for the Hypersphere](https://arxiv.org/abs/2606.17603) | - |
| 2026 | SSRN | FAR-JEPA | [FAR-JEPA: Factorized Autoregressive Process Laws for Resolving the Orthogonal Gauge in Joint Embeddings](https://doi.org/10.2139/ssrn.7173858) | - |
| 2026 | arXiv | Func-JEPA | [Func-JEPA: Learning a Sobolev Space of Functions as Latent Vectors](https://arxiv.org/abs/2611.19542) | [Code](https://github.com/amorarc/Func-JEPA) |
| 2026 | arXiv | - | [Good Views Are Not Enough: Global Counterexamples for Gaussian-Regularized JEPAs](https://arxiv.org/abs/2611.12137) | - |
| 2026 | SSRN | - | [Identifiability and Latent Geometry of Joint-embedding Predictive World Models](https://doi.org/10.2139/ssrn.7158998) | - |
| 2026 | arXiv | - | [JEPA Learns What the Mask Leaves Unrecoverable](https://arxiv.org/abs/2609.32481) | - |
| 2026 | arXiv | LocaLeJEPA | [LocaLeJEPA: Maximum Entropy Representations under Geometric Priors](https://arxiv.org/abs/2610.28458) | [Code](https://github.com/alessioborgi/LocaLeJEPA) |
| 2026 | arXiv | MM-LeJEPA | [MM-LeJEPA: Correlated Gaussian Regularization for Multimodal Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2610.24681) | - |
| 2026 | HAL | - | [On the Information Bottleneck of VJEPA](https://doi.org/10.5281/zenodo.20173025) | - |
| 2026 | arXiv | - | [Proving and Improving the Platonic Representation Hypothesis with JEPAs](https://arxiv.org/abs/2610.39302) | - |
| 2026 | arXiv | - | [Same-State Pairs Make One JEPA Proof of the Platonic Representation Hypothesis Vacuous](https://arxiv.org/abs/2611.16182) | - |
| 2026 | arXiv | - | [Shared Gaussianization: What Gaussian Regularizers Certify About Contrastive Learning, and What They Miss](https://arxiv.org/abs/2610.10299) | - |
| 2026 | arXiv | - | [Shared Is Not Enough: Predictor Width and Factor Readability Under Masked Latent Prediction](https://arxiv.org/abs/2610.32562) | - |
| 2026 | arXiv | Social-JEPA | [Social-JEPA: Emergent Geometric Isomorphism](https://arxiv.org/abs/2603.02263) | - |
| 2026 | arXiv | SPHERE-JEPA | [SPHERE-JEPA: Spherical Prediction with Homogeneous Embeddings](https://arxiv.org/abs/2605.26900) | - |
| 2026 | LNCS | Stylistic-STORM (ST-STORM) | [Stylistic-STORM (ST-STORM): Self-supervised Spectral Disentanglement Using Adversarial Learning and JEPA for Weather Analysis](https://doi.org/10.1007/978-3-032-31673-8_1) | - |
| 2026 | arXiv | - | [The SIGReg Objective as Variational Free Energy: A Theoretical Active-Inference Account of JEPA World Models](https://arxiv.org/abs/2607.13612) | - |
| 2026 | arXiv | UR-JEPA | [UR-JEPA: Uniform Rectifiability as a Regularizer for Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2606.01443) | - |
| 2026 | ICML | Var-JEPA | [Var-JEPA: A Variational Formulation of the Joint-Embedding Predictive Architecture - Bridging Predictive and Generative Self-Supervised Learning](https://arxiv.org/abs/2603.20111) | - |
| 2026 | arXiv | VISReg | [VISReg: Variance-Invariance-Sketching Regularization for JEPA training](https://arxiv.org/abs/2606.02572) | [Project](https://haiyuwu.github.io/visreg) |
| 2026 | NeurIPS | - | [When Does LeJEPA Learn a World Model?](https://arxiv.org/abs/2605.26379) | [Code](https://github.com/klindtlab/lejepa-identifiability) |
| 2026 | SSRN | - | [When Isotropy Fails: Selecting a JEPA's Collapse-Avoidance Geometry from the Data Distribution](https://doi.org/10.2139/ssrn.7536198) | - |
| 2026 | arXiv | - | [Your Probabilistic JEPA Is Secretly a Hidden Markov Model: A State-Space Interpretation of Joint-Embedding Predictive Learning](https://arxiv.org/abs/2608.13621) | - |
| 2025 | arXiv | - | [Gaussian Embeddings: How JEPAs Secretly Learn Your Data Density](https://arxiv.org/abs/2510.05949) | - |
| 2025 | arXiv | KerJEPA | [KerJEPA: Kernel Discrepancies for Euclidean Self-Supervised Learning](https://arxiv.org/abs/2512.19605) | - |
| 2025 | arXiv | LeJEPA | [LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics](https://arxiv.org/abs/2511.08544) | [Code](https://github.com/rbalestr-lab/lejepa) |
| 2025 | arXiv | - | [Why and How Auxiliary Tasks Improve JEPA Representations](https://arxiv.org/abs/2509.12249) | - |
| 2024 | NeurIPS | - | [How JEPA Avoids Noisy Features: The Implicit Bias of Deep Linear Self Distillation Networks](https://arxiv.org/abs/2407.03475) | - |
| 2024 | arXiv | - | [Sora and V-JEPA Have Not Learned The Complete Real World Model -- A Philosophical Analysis of Video AIs Through the Theory of Productive Imagination](https://arxiv.org/abs/2407.10311) | - |

### JEPA-F: Image and Static Representation Learning

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | SSRN | - | [A Novel Approach to Pavement Crack Classification using Joint-Embedding Predictive Architectures](https://doi.org/10.2139/ssrn.7198799) | - |
| 2026 | Neural Processing Letters | - | [Adaptive Sports Optimization Framework Based on I-JEPA: Standing Long Jump Performance Prediction and PSO Trajectory Optimization](https://doi.org/10.1007/s11063-026-11865-y) | - |
| 2026 | arXiv | - | [Attention-Only White-Box Transformer via LeJEPA-Based Self-Supervised Pretraining](https://arxiv.org/abs/2608.04213) | - |
| 2026 | IEEE International Conference on Document Analysis and… | Bar-JEPA | [Bar-JEPA: Extracting Values from Bar Chart with Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2608.06062) | [Code](https://github.com/dralois/Bar-JEPA) |
| 2026 | arXiv | - | [Beyond Generative Priors: Minority Sampling with JEPA-Guided Diffusion](https://arxiv.org/abs/2605.24631) | [Code](https://github.com/soobin-um/jepa-guidance) |
| 2026 | arXiv | BiJEPA | [BiJEPA: Bi-directional Joint Embedding Predictive Architecture for Symmetric Representation Learning](https://arxiv.org/abs/2603.00049) | - |
| 2026 | arXiv | - | [Context-Predictive Low-Rank Adaptation for Face Presentation Attack Detection](https://arxiv.org/abs/2611.16534) | - |
| 2026 | ICML Workshop | DLLM-JEPA | [DLLM-JEPA: Joint Embedding Predictive Architectures for Masked Diffusion Language Models](https://arxiv.org/abs/2606.00091) | - |
| 2026 | ECCV | DSeq-JEPA | [DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2511.17354) | [Project](https://dseqjepa-project.com) |
| 2026 | LNCS | - | [Energy-Based Hyperparameter Optimization for Joint-Embedding Predictive Architectures](https://doi.org/10.1007/978-981-92-5870-3_26) | - |
| 2026 | CVIU | - | [Escaping The Big Data Paradigm in Self-Supervised Representation Learning](https://arxiv.org/abs/2502.18056) | [Code](https://github.com/inescopresearch/scott) |
| 2026 | AAAI Workshop | - | [Exploring Joint-Embedding Predictive Architectures for Self-Supervised Representation Learning of Powder X-ray Diffraction Patterns](https://arxiv.org/abs/2610.33310) | - |
| 2026 | arXiv | - | [From Alignment to Prediction: A Study of Self-Supervised Learning and Predictive Representation Learning](https://arxiv.org/abs/2604.13518) | - |
| 2026 | arXiv | HQ-JEPA | [HQ-JEPA: Hybrid Quantum Joint-Embedding Predictive Architecture for Cross-Modal Remote Sensing Representation Learning](https://arxiv.org/abs/2605.31068) | - |
| 2026 | arXiv | - | [Is the reconstruction loss culprit? An attempt to outperform JEPA](https://arxiv.org/abs/2603.14131) | - |
| 2026 | ECML PKDD | JEPAMatch | [JEPAMatch: Geometric Representation Shaping for Semi-Supervised Learning](https://arxiv.org/abs/2604.21046) | - |
| 2026 | arXiv | - | [Joint-Embedding Predictive Architecture for Solar PV Panel Fault Classification](https://arxiv.org/abs/2607.09205) | [Code](https://github.com/Azimi2kht/JEFFNet) |
| 2026 | arXiv | - | [Knowledge, Rules and Their Embeddings: Two Paths towards Neuro-Symbolic JEPA](https://arxiv.org/abs/2603.13265) | - |
| 2026 | arXiv | LEF-JEPA | [LEF-JEPA: Denoising-Trained Latent Energy Fields for Spatial Representation Learning](https://arxiv.org/abs/2611.08989) | - |
| 2026 | arXiv | - | [Mask-supervised Object-centric Representation Learning with LeJEPA](https://arxiv.org/abs/2607.02404) | - |
| 2026 | CVPR Workshop | Mine-JEPA | [Mine-JEPA: In-Domain Self-Supervised Learning for Mine-Like Object Classification in Side-Scan Sonar](https://arxiv.org/abs/2604.00383) | - |
| 2026 | Signal Processing and Communications Applications… | - | [Noise-guided Masking for Image-based Joint-Embedding Predictive Architectures](https://doi.org/10.1109/siu71813.2026.11636521) | - |
| 2026 | NeurIPS | PEIRA | [PEIRA: Learning Predictive Encoders through Inter-View Regressor Alignment](https://arxiv.org/abs/2605.17671) | [Code](https://github.com/MichaelArbel/peira-loss) |
| 2026 | arXiv | - | [Predicting Functions, Not Features: KANs with Function-Space Joint-Embedding Predictive Learning for Medical Image Segmentation](https://arxiv.org/abs/2608.12050) | - |
| 2026 | Pattern Recognition Letters | - | [Probabilistic image-based joint embedding predictive architecture](https://doi.org/10.1016/j.patrec.2026.07.005) | - |
| 2026 | engrXiv | - | [Robustness Evaluation of a JEPA-Based Model and YOLO for Pavement Distress Classification under Noise Corruptions](https://doi.org/10.31224/7375) | - |
| 2026 | arXiv | - | [Scaling Representation Diversity: Modulated Attention and Reconstructive Regularization for Visual Grounding](https://arxiv.org/abs/2608.12748) | - |
| 2026 | arXiv | SiamJEPA | [SiamJEPA: On the Role of Siamese Student Encoders in JEPA](https://arxiv.org/abs/2607.04044) | [Code](https://github.com/oist/SiamJEPA) |
| 2026 | ACM MM | Swap-JEPA | [Swap-JEPA: Learning Latent Correspondences for Zero-shot Object Swapping in Live Shopping](https://doi.org/10.1145/3767308.3835350) | - |
| 2026 | arXiv | The JEPA Predictor | [The JEPA Predictor: A Transferable Operator for Occluded Feature Completion](https://arxiv.org/abs/2607.16274) | - |
| 2025 | International Conference on Image and Vision Computing… | - | [Comparative Study of DINOv2, I-JEPA, and ViT Embeddings for Unsupervised Anomaly Detection](https://doi.org/10.1109/ivcnz67716.2025.11281645) | - |
| 2025 | arXiv | Discrete JEPA | [Discrete JEPA: Learning Discrete Token Representations without Reconstruction](https://arxiv.org/abs/2506.14373) | - |
| 2025 | arXiv | - | [Elucidating the Role of Feature Normalization in IJEPA](https://arxiv.org/abs/2508.02829) | - |
| 2025 | CVIU | - | [Exploring joint embedding predictive architectures for pretraining convolutional neural networks](https://doi.org/10.1016/j.cviu.2025.104595) | - |
| 2025 | arXiv | - | [Improving Joint Embedding Predictive Architecture with Diffusion Noise](https://arxiv.org/abs/2507.15216) | - |
| 2025 | arXiv | - | [Predict, Cluster, Refine: A Joint Embedding Predictive Self-Supervised Framework for Graph Representation Learning](https://arxiv.org/abs/2502.01684) | [Code](https://github.com/Deceptrax123/JPEB-GSSL) |
| 2025 | arXiv | SparseJEPA | [SparseJEPA: Sparse Representation Learning of Joint Embedding Predictive Architectures](https://arxiv.org/abs/2504.16140) | - |
| 2025 | ICLR | T-JEPA | [T-JEPA: Augmentation-Free Self-Supervised Learning for Tabular Data](https://arxiv.org/abs/2410.05016) | - |
| 2024 | International Conference on Machine Learning and… | CNN-JEPA | [CNN-JEPA: Self-Supervised Pretraining Convolutional Neural Networks Using Joint Embedding Predictive Architecture](https://arxiv.org/abs/2408.07514) | - |
| 2024 | NeurIPS | - | [Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning](https://arxiv.org/abs/2410.19560) | - |
| 2024 | ICLR | - | [Denoising with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2410.03755) | - |
| 2024 | arXiv | DMT-JEPA | [DMT-JEPA: Discriminative Masked Targets for Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2405.17995) | [Code](https://github.com/DMTJEPA/DMTJEPA) |
| 2024 | NeurIPS Workshop | - | [Enhancing JEPAs with Spatial Conditioning: Robust and Efficient Representation Learning](https://arxiv.org/abs/2410.10773) | - |
| 2024 | arXiv | - | [High-Resolution Image Synthesis via Next-Token Prediction](https://arxiv.org/abs/2411.14808) | - |
| 2024 | arXiv | - | [Joint-Embedding Predictive Architecture for Self-Supervised Learning of Mask Classification Architecture](https://arxiv.org/abs/2407.10733) | - |
| 2024 | arXiv | - | [Recurrent Joint Embedding Predictive Architecture with Recurrent Forward Propagation Learning](https://arxiv.org/abs/2411.16695) | - |
| 2023 | CVPR | I-JEPA | [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243) | - |

### JEPA-T: Video and Temporal Prediction

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | ECCV Workshop | - | [A Framework for Egocentric and Exocentric Procedural Understanding via Temporal Segmentation and Semantic Abstraction](https://arxiv.org/abs/2610.00069) | - |
| 2026 | SSRN | - | [Auditing Adjacent JEPA Versions: Real-Subset Evaluation and Late Causal Divergence in V-JEPA 2 and V-JEPA 2.1](https://doi.org/10.2139/ssrn.6482015) | - |
| 2026 | arXiv | Branch-JEPA | [Branch-JEPA: Finite-Support Predictive Distributions for JEPA World Models](https://arxiv.org/abs/2607.05238) | - |
| 2026 | Knowledge-Based Systems | CF-JEPA | [CF-JEPA: Mask-free forward prediction with asymmetric encoder utilization for time-series representation learning](https://arxiv.org/abs/2606.07031) | - |
| 2026 | International Conference on Big Data and Information… | CSCI-VJEPA | [CSCI-VJEPA: Injecting Latent Predictive Tokens for Cloth-Changing Video Re-Identification](https://doi.org/10.1109/bigdia71496.2026.11684540) | - |
| 2026 | Preprints.org | - | [Distributional Objectives for VJEPA](https://doi.org/10.20944/preprints202610.2122.v1) | - |
| 2026 | International Conference on Information and Computer… | - | [Efficient Human Action Recognition with Mixed-Precision V-JEPA on Embedded Devices](https://doi.org/10.1145/3803291.3803358) | - |
| 2026 | arXiv | - | [Entity-Centric World Models: Interaction-Aware Masking for Causal Video Prediction](https://arxiv.org/abs/2605.15466) | - |
| 2026 | arXiv | EV-JEPA | [EV-JEPA: Elastic V-JEPA for Any Device and Cross-Device Inference](https://arxiv.org/abs/2610.14324) | - |
| 2026 | arXiv | - | [Factorized Latent Dynamics for Video JEPA: An Empirical Study of Auxiliary Objectives](https://arxiv.org/abs/2605.17165) | - |
| 2026 | arXiv | Fovea-JEPA | [Fovea-JEPA: Overcoming Geometric Blind Spots in V-JEPA for Camera Motion Recognition](https://arxiv.org/abs/2610.34033) | - |
| 2026 | TCSVT | GOT-JEPA | [GOT-JEPA: Generic Object Tracking with Model Adaptation and Occlusion Handling using Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2602.14771) | - |
| 2026 | arXiv | Human-JEPA | [Human-JEPA: A Human-Centric Vision Model that Perceives and Anticipates](https://arxiv.org/abs/2608.21160) | - |
| 2026 | arXiv | IMPULSE | [IMPULSE: Push First, Then Predict in V-JEPA 2 Feature Space](https://arxiv.org/abs/2610.23968) | - |
| 2026 | arXiv | - | [Interpreting Physics in Video Encoders using Multi-Object Interaction Videos](https://arxiv.org/abs/2610.31983) | - |
| 2026 | bioRxiv | JEPA-SORT | [JEPA-SORT: World-Model Embeddings Improve Deep-Sea Multi-Object Tracking on Visually Homogeneous Fauna](https://doi.org/10.64898/2026.10.07.757484) | - |
| 2026 | CVPR Workshop | JFAA | [JFAA: Technical Report for the EPIC-KITCHENS-100 Action Anticipation Challenge at EgoVis 2026](https://arxiv.org/abs/2605.20904) | [Code](https://github.com/CorrineQiu/JFAA) |
| 2026 | arXiv | - | [Latent Clarity: Bridging World-Model Kinematics to Semantic Manifolds for Video Anomaly Anticipation](https://arxiv.org/abs/2607.03558) | - |
| 2026 | arXiv | LeVJEPA | [LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics](https://arxiv.org/abs/2608.27395) | - |
| 2026 | arXiv | MotionJEPA | [MotionJEPA: Preventing Temporal Feature Collapse by Capturing Visual Changes in Latent Space](https://arxiv.org/abs/2609.23881) | [Code](https://github.com/mkarmann/motion-jepa) |
| 2026 | arXiv | MV-JEPA | [MV-JEPA: Post-Training Video Encoders for Cross-View Understanding](https://arxiv.org/abs/2611.25172) | - |
| 2026 | arXiv | OccJEPA | [OccJEPA: Occlusion as Masking for Amodal Video Segmentation](https://arxiv.org/abs/2610.29061) | [Code](https://github.com/zgp110/occjepa) |
| 2026 | arXiv | - | [One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617) | [Code](https://github.com/showlab/O2LaF) |
| 2026 | arXiv | P-JEPA | [P-JEPA: Procedural Video Representation Learning via Joint Embedding Predictive Architecture](https://arxiv.org/abs/2606.23256) | - |
| 2026 | arXiv | PhysVideoGenerator | [PhysVideoGenerator: Towards Physically Aware Video Generation via Latent Physics Guidance](https://arxiv.org/abs/2601.03665) | [Code](https://github.com/CVFall2025-Project/PhysVideoGenerator) |
| 2026 | NeurIPS Workshop | - | [Reconstruction vs. Prediction Pre-Training of Discrete Video Representations for Continuous Control](https://arxiv.org/abs/2611.24781) | - |
| 2026 | IEEE Conference on Cybernetics and Intelligent Systems | - | [Serial Cycle-Consistent Video Joint Embedding Predictive Architecture with Phase-Wise Optimization](https://doi.org/10.1109/cis-ram71614.2026.11668547) | - |
| 2026 | arXiv | SPACE | [SPACE: Sparse Predictive Attractor via Counterfactual Eviction for Streaming Video Memory](https://arxiv.org/abs/2609.32592) | - |
| 2026 | CVPR Workshop | TAP-JEPA | [TAP-JEPA: Frozen Future-Latent Probing and Two-Stage Score Fusion for EPIC-KITCHENS-100 Action Anticipation](https://arxiv.org/abs/2606.00662) | - |
| 2026 | ECCV Workshop | - | [Unifying Semantic Priors and High-Frequency Traces: Enhancing V-JEPA with Mixture-of-Experts for Robust Synthetic Image Forensics](https://arxiv.org/abs/2609.16778) | [Code](https://github.com/ALCOR-Lab-DIAG/MoE-JEPA) |
| 2026 | arXiv | UWM-JEPA | [UWM-JEPA: Predictive World Models That Imagine in Belief Space](https://arxiv.org/abs/2605.25313) | [Code](https://github.com/santoshkumarradha/uwm-jepa) |
| 2026 | arXiv | - | [V-JEPA 2 Meets AQA: Phase-Based Scoring and Reference-Based Feedback for Mountain Biking](https://arxiv.org/abs/2610.30160) | - |
| 2026 | ECCV | V-JEPA 2.1 | [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482) | - |
| 2026 | arXiv | V-JEPA Hand | [V-JEPA Hand: Simple, Accurate and Fast 3D Hand and Camera Trajectory Recovery from Egocentric Videos](https://arxiv.org/abs/2610.26780) | [Project](https://qft-333.github.io/V-JEPA-Hand-Page/) |
| 2026 | CVPR Workshop | VISTA | [VISTA: Technical Report for the Ego4D Short-Term Object Interaction Anticipation at EgoVis 2026](https://arxiv.org/abs/2605.20901) | [Code](https://github.com/CorrineQiu/VISTA) |
| 2026 | arXiv | VR-JEPA | [VR-JEPA: Learning Contrastive-State Latent Guidance for Generation-based Video Reasoning](https://arxiv.org/abs/2609.40129) | - |
| 2025 | arXiv | - | [Behavioral Geometric Supervision Aligns Video Foundation Models with Human Social Perception](https://arxiv.org/abs/2510.01502) | - |
| 2025 | ICLR | Beyond FVD | [Beyond FVD: Enhanced Evaluation Metrics for Video Generation Quality](https://arxiv.org/abs/2410.05203) | - |
| 2025 | NeurIPS | - | [Grounding Foundational Vision Models with 3D Human Poses for Robust Action Recognition](https://arxiv.org/abs/2511.05622) | [Code](https://github.com/nbabey20/groundactrec) |
| 2025 | IEEE International Symposium on Robot and Human… | - | [How do Foundation Models Compare to Skeleton-Based Approaches for Gesture Recognition in Human-Robot Interaction?](https://arxiv.org/abs/2506.20795) | - |
| 2025 | ICCV | - | [Improving the Physics of Video Generation with VJEPA-2 Reward Signal](https://arxiv.org/abs/2510.21840) | - |
| 2025 | AJEA | nano-JEPA | [nano-JEPA: Una propuesta para posibilitar la interpretación de video usando computadoras personales](https://rtyc.utn.edu.ar/index.php/ajea/article/view/1875) | - |
| 2025 | ICLR | Rethinking JEPA | [Rethinking JEPA: Compute-Efficient Video SSL with Frozen Teachers](https://arxiv.org/abs/2509.24317) | - |
| 2025 | arXiv | - | [Temporal vs. Spatial: Comparing DINOv3 and V-JEPA2 Feature Representations for Video Action Analysis](https://arxiv.org/abs/2509.21595) | - |
| 2025 | arXiv | V-JEPA 2 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) | - |
| 2025 | Affective Computing and Intelligent Interaction | - | [Video Joint-Embedding Predictive Architectures for Facial Expression Recognition](https://arxiv.org/abs/2601.09524) | [Code](https://github.com/lennarteingunia/vjepa-for-fer) |
| 2024 | IEEE International Conference on Big Data | Animal-JEPA | [Animal-JEPA: Advancing Animal Behavior Studies Through Joint Embedding Predictive Architecture in Video Analysis](https://doi.org/10.1109/bigdata62323.2024.10826081) | - |
| 2024 | NeurIPS Workshop | - | [Joint Embeddings Go Temporal](https://arxiv.org/abs/2509.25449) | - |
| 2024 | arXiv | TWLV-I | [TWLV-I: Analysis and Insights from Holistic Evaluation on Video Foundation Models](https://arxiv.org/abs/2408.11318) | [Code](https://github.com/twelvelabs-io/video-embeddings-evaluation-framework) |
| 2024 | arXiv | - | [Video Representation Learning with Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2412.10925) | - |
| 2023 | arXiv | MC-JEPA | [MC-JEPA: A Joint-Embedding Predictive Architecture for Self-Supervised Learning of Motion and Content Features](https://arxiv.org/abs/2307.12698) | - |

### JEPA-A: Action-Conditioned World Models, Planning and Control

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | ICLR Workshop | - | [A Lightweight Library for Energy-Based Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2602.03604) | [Code](https://github.com/facebookresearch/eb_jepa) |
| 2026 | arXiv | ACG-WAM | [ACG-WAM: World-Action Modeling via Action-Conditioned Geometric Latent Prediction](https://arxiv.org/abs/2610.06965) | [Code](https://github.com/RoboOpus/ACG-WAM.Website:https://RoboOpus.github.io/ACG-WAM) |
| 2026 | IEEE Access | ACT-JEPA | [ACT-JEPA: Novel Joint-Embedding Predictive Architecture for Efficient Policy Representation Learning](https://arxiv.org/abs/2501.14622) | - |
| 2026 | arXiv | ActWorld-JEPA | [ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2611.16579) | [Code](https://github.com/adept-thu/ActWorld-JEPA) |
| 2026 | arXiv | - | [Adaptive Latent Capacity for World Models](https://arxiv.org/abs/2609.32921) | - |
| 2026 | arXiv | Aero-VPA | [Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware](https://arxiv.org/abs/2611.04392) | [Code](https://github.com/ylee-sling/Aero-VPA) |
| 2026 | HAL | Agentic-JEPA | [Agentic-JEPA: A Self-Supervised World Model for Planning in Text-Based Agent Environments](https://hal.science/hal-05546567) | - |
| 2026 | arXiv | - | [Anisotropic Representations Improve Planning in JEPA World Models](https://arxiv.org/abs/2609.37441) | [Project](https://rkdrn79.github.io/AnisoWM-page/) |
| 2026 | arXiv | ARC-Bench | [ARC-Bench: Closed-Loop Replanning Masks Broken Action Ranking in Frozen JEPA World Models](https://arxiv.org/abs/2609.05461) | - |
| 2026 | arXiv | AVL-JEPA | [AVL-JEPA: Preventing Causal Dynamics Information Collapse In Joint Embedding Predictive Architecture World Models](https://arxiv.org/abs/2610.03587) | - |
| 2026 | arXiv | - | [Behavioral Monitoring of JEPA World Models with Jacobian Centroids](https://arxiv.org/abs/2609.33940) | - |
| 2026 | arXiv | BeJEPA | [BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL](https://arxiv.org/abs/2610.23127) | [Project](https://ylyem9x.github.io/BeJEPA-project) |
| 2026 | arXiv | BeliefGraph-JEPA | [BeliefGraph-JEPA: Structured Latent World Models for Action-Conditioned Time Series](https://arxiv.org/abs/2610.05409) | - |
| 2026 | arXiv | - | [Beyond Action Prediction: Learning Search-Free Planning in Latent Space](https://arxiv.org/abs/2610.23615) | - |
| 2026 | arXiv | - | [Bilinear World Models: Learning Representations with Structured Dynamics for Efficient Control](https://arxiv.org/abs/2609.36305) | - |
| 2026 | arXiv | BRo-JEPA | [BRo-JEPA: Learning Modular Transformations in Latent Space](https://arxiv.org/abs/2606.01372) | [Code](https://github.com/DL-World-Models/brojepa) |
| 2026 | arXiv | - | [Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields](https://arxiv.org/abs/2608.17496) | - |
| 2026 | arXiv | CF-JEPA | [CF-JEPA: Improving Robustness of JEPA World Models via Controllability Factorization](https://arxiv.org/abs/2610.00727) | [Project](https://morganbyrd03.github.io/cf-jepa/) |
| 2026 | NeurIPS Workshop | - | [Counterfactual Action Evaluation, Observation Bottlenecks, and Representation Geometry in Joint-Embedding Predictive World Models](https://arxiv.org/abs/2610.02860) | - |
| 2026 | arXiv | - | [Counterfactual World Models: JEPAs That Reason About "What If"](https://arxiv.org/abs/2611.24778) | - |
| 2026 | arXiv | - | [Coupled Control and Wireless World Models for Resilient Remote Robotic Control](https://arxiv.org/abs/2609.04851) | - |
| 2026 | arXiv | D-JEPA | [D-JEPA: A Decision-Aligned Latent World Model](https://arxiv.org/abs/2609.24749) | - |
| 2026 | arXiv | DA-WAM | [DA-WAM: Decision-Aligned Future Latents for Driving World Models](https://arxiv.org/abs/2608.19085) | - |
| 2026 | arXiv | DeepJEPA | [DeepJEPA: Scaling World Models from Within](https://arxiv.org/abs/2610.00368) | [Project](https://deepjepa.github.io/) |
| 2026 | arXiv | Delta-JEPA | [Delta-JEPA: Learning Action-Sensitive World Models via Latent Difference Decoding](https://arxiv.org/abs/2606.31232) | - |
| 2026 | arXiv | Demo-JEPA | [Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation](https://arxiv.org/abs/2605.20811) | - |
| 2026 | arXiv | DepState-JEPA | [DepState-JEPA: Learning Depth-Grounded State Representation for Visual Perception and Manipulation](https://arxiv.org/abs/2610.29246) | [Project](https://shawnleung-sii.github.io/depstate-jepa/) |
| 2026 | arXiv | - | [Depth-Regularized JEPA World Models Learn More Transferable Representations from Real Outdoor Robot Data](https://arxiv.org/abs/2607.16314) | - |
| 2026 | arXiv | - | [Detecting is Easy, Adapting is Hard: Local Expert Growth for Visual Model-Based Reinforcement Learning under Distribution Shift](https://arxiv.org/abs/2604.27411) | - |
| 2026 | arXiv | - | [Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency](https://arxiv.org/abs/2608.12939) | - |
| 2026 | arXiv | - | [Diffusion-Steering-Based MPC with a JEPA World Action Model](https://arxiv.org/abs/2610.12407) | - |
| 2026 | arXiv | Do-JEPA | [Do-JEPA: From Masking to Intervention in Latent World Models](https://arxiv.org/abs/2609.37378) | - |
| 2026 | arXiv | - | [Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations and Goals](https://arxiv.org/abs/2608.29434) | - |
| 2026 | arXiv | DT-JEPA | [DT-JEPA: Learning to Predict Future Representations for Decision-Making](https://arxiv.org/abs/2610.32657) | - |
| 2026 | arXiv | - | [Efficient Hierarchical Implicit Flow Q-learning for Offline Goal-conditioned Reinforcement Learning](https://arxiv.org/abs/2604.08960) | - |
| 2026 | ACM MM | - | [Efficient Rationale-based Retrieval: On-policy Distillation from Generative Rerankers based on JEPA](https://arxiv.org/abs/2604.23336) | - |
| 2026 | arXiv | EgoJEPA | [EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos](https://arxiv.org/abs/2610.20904) | - |
| 2026 | NeurIPS | EpicWorldModel | [EpicWorldModel: Exploration-driven Planning with Latent World Models](https://arxiv.org/abs/2610.05996) | - |
| 2026 | arXiv | EPM-JEPA | [EPM-JEPA: Operator-Side Experience Modulation in JEPA-Family World Models](https://arxiv.org/abs/2606.12979) | - |
| 2026 | arXiv | - | [Exploring Temporal Context-Aware Physical Grounding in Latent World Models](https://arxiv.org/abs/2610.28483) | [Code](https://github.com/myl11045/G-JEPA) |
| 2026 | arXiv | FactorJEPA | [FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels for Crowded and Chaotic Global South Urban Worlds](https://arxiv.org/abs/2608.01049) | [Code](https://huggingface.co/datasets/anonymousML123/denseworld-115k) |
| 2026 | arXiv | Fast-JEPA | [Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models](https://arxiv.org/abs/2611.25927) | [Code](https://github.com/Sofilyzia/Fast-JEPA) |
| 2026 | arXiv | FF-JEPA | [FF-JEPA: Long-Horizon Planning in World Models with Latent Planners](https://arxiv.org/abs/2606.09311) | - |
| 2026 | arXiv | FlexiWorld | [FlexiWorld: Learning and Planning via Flexible Action Chunks Across Multiple Time Scales](https://arxiv.org/abs/2609.35138) | [Project](https://shidu-ren.github.io/FlexiWorld-Project-Page/) |
| 2026 | arXiv | Flow-JEPA | [Flow-JEPA: Robust Latent Dynamics for JEPA World Models via Flow Matching](https://arxiv.org/abs/2608.29029) | - |
| 2026 | arXiv | - | [Frozen in a Frame: The Velocity Blind Spot in JEPA World Models](https://arxiv.org/abs/2610.04585) | - |
| 2026 | CVPR | GeoWorld | [GeoWorld: Geometric World Models](https://arxiv.org/abs/2602.23058) | [Project](https://steve-zeyu-zhang.github.io/GeoWorld) |
| 2026 | Research Square | Ground-JEPA | [Ground-JEPA: Learning Physically Grounded Latent World Models for Zero-Shot Dynamics Generalization of Legged Robots](https://doi.org/10.21203/rs.3.rs-10511499/v1) | - |
| 2026 | arXiv | GUI-JEPA | [GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents](https://arxiv.org/abs/2610.36877) | [Code](https://github.com/bcwang-sjtu/GUI-JEPA) |
| 2026 | arXiv | H-JEPA | [H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning](https://arxiv.org/abs/2610.06805) | - |
| 2026 | arXiv | Hamiltonian JEPA | [Hamiltonian JEPA: Action-Conditioned World Models with an Inherited Control State](https://arxiv.org/abs/2609.33497) | - |
| 2026 | arXiv | HanoiWorld | [HanoiWorld : A Joint Embedding Predictive Architecture BasedWorld Model for Autonomous Vehicle Controller](https://arxiv.org/abs/2601.01577) | - |
| 2026 | arXiv | - | [I Act Therefore I Am: When Is JEPA's Action-Conditioning Enough to Learn Causal Mechanisms?](https://arxiv.org/abs/2609.31161) | - |
| 2026 | arXiv | InJePA | [InJePA: Intention-First Latent Planning with Coupled JEPA World Models for Visual Navigation](https://arxiv.org/abs/2610.23896) | [Code](https://github.com/zhuxun132/InJepa) |
| 2026 | arXiv | Inside-JEPA | [Inside-JEPA: From Prediction to Relational Grounding in Latent World Models](https://arxiv.org/abs/2610.31194) | - |
| 2026 | arXiv | INTACT | [INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models](https://arxiv.org/abs/2607.26056) | - |
| 2026 | arXiv | - | [Intrinsic-Energy Joint Embedding Predictive Architectures Induce Quasimetric Spaces](https://arxiv.org/abs/2602.12245) | - |
| 2026 | arXiv | - | [Is Forward Prediction Enough? Physical State Grounding for JEPA World Models](https://arxiv.org/abs/2608.06799) | - |
| 2026 | arXiv | JEDI | [JEDI: Joint Embedding Diffusion World Model for Online Model-Based Reinforcement Learning](https://arxiv.org/abs/2605.13013) | - |
| 2026 | arXiv | JEDI | [JEDI: Joint-Embedding Demonstration Compression for In-Context Imitation Learning](https://arxiv.org/abs/2610.40356) | - |
| 2026 | arXiv | JEPA Dots | [JEPA Dots: Dual-Latent World Model for Language-Guided Robot Control](https://arxiv.org/abs/2611.24062) | - |
| 2026 | arXiv | JEPA Policy | [JEPA Policy: Diffusion-Free Imitation Learning via Paired Action and Future Representation Prediction](https://arxiv.org/abs/2609.09630) | [Code](https://github.com/jiejie567/JEPA-Policy) |
| 2026 | arXiv | JEPA-Bisim | [JEPA-Bisim: Learning Robust Visual Representations for Planning with Joint-Embedding Predictive World Models](https://arxiv.org/abs/2602.18639) | - |
| 2026 | NeurIPS Workshop | JEPA-TTT | [JEPA-TTT: Persistent Test-Time Training of Latent World Models for Planning under Dynamics Shifts](https://arxiv.org/abs/2610.00722) | [Project](https://jepa-ttt.github.io/) |
| 2026 | arXiv | JEPA-VLA | [JEPA-VLA: Video Predictive Embedding is Needed for VLA Models](https://arxiv.org/abs/2602.11832) | - |
| 2026 | arXiv | JEPA-WAM | [JEPA-WAM: Connecting Generated Visual Instructions to World Action Models through JEPA Latent Representations](https://arxiv.org/abs/2609.20277) | - |
| 2026 | arXiv | JEPA-WAM | [JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling](https://arxiv.org/abs/2608.09381) | [Project](https://spritewithoutice.github.io/JEPA_WAM/) |
| 2026 | arXiv | JEPA-x | [JEPA-x: Cross-Predictive Physics Grounding for Forecastable Latent Dynamics](https://arxiv.org/abs/2608.24044) | - |
| 2026 | arXiv | JEPA4R | [JEPA4R: Embodied JEPA World Models with 4D Point Planning](https://arxiv.org/abs/2611.19771) | [Code](https://github.com/AIGeeksGroup/JEPA4R) |
| 2026 | arXiv | JEPLO | [JEPLO: Joint-Embedding Predictive Learning for LiDAR-Based Legged Locomotion](https://arxiv.org/abs/2609.15770) | [Code](https://github.com/ASIG-X/JEPLO) |
| 2026 | arXiv | JEPTERA | [JEPTERA: A Platform Agnostic JEPA-Assisted Model Predictive Planner for Urban UAV Navigation](https://arxiv.org/abs/2611.20593) | - |
| 2026 | Preprints.org | Jev-JEPA | [Jev-JEPA: Language-Programmable Semantic Priors for Joint-Embedding World Model Control](https://doi.org/10.20944/preprints202610.0229.v1) | - |
| 2026 | arXiv | Juno | [Juno: Taming Predictive Latents for Vision-Language-Action Models](https://arxiv.org/abs/2610.09940) | [Project](https://juno-policy.github.io/) |
| 2026 | arXiv | - | [Keeping JEPA World Models Plannable When Little of the Frame Moves](https://arxiv.org/abs/2610.03137) | - |
| 2026 | arXiv | La-JEPA | [La-JEPA: Compact Robot Policies with Latent World Modeling](https://arxiv.org/abs/2611.08156) | [Code](https://github.com/mt-clemente/lajepa) |
| 2026 | NeurIPS | - | [Latent Video Prediction for World Modeling: An Evaluation Uncovering Intriguing Favorable Evidence](https://arxiv.org/abs/2605.15618) | - |
| 2026 | arXiv | LATER | [LATER: Learning Action-Conditioned Temporal Evidence Retrieval for Predictive World Models](https://arxiv.org/abs/2611.25671) | - |
| 2026 | arXiv | LeapBot-WA | [LeapBot-WA: World-Anchor Action Models via Predictive Latent Alignments](https://arxiv.org/abs/2607.23969) | [Code](https://github.com/LeapWM/leapbot-wa) |
| 2026 | arXiv | LeHami | [LeHami: Symplectic Latent Dynamics for World Models](https://arxiv.org/abs/2610.15267) | - |
| 2026 | arXiv | LeWAM | [LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/abs/2610.12818) | [Project](https://le-wam.github.io/) |
| 2026 | arXiv | LeWAM | [LeWAM: Latent evolving World Action Model](https://arxiv.org/abs/2609.27455) | [Code](https://github.com/XuejiFang/LeWAM) |
| 2026 | arXiv | LeWM | [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/abs/2603.19312) | - |
| 2026 | arXiv | LpWM | [LpWM: A Case for Sparse Representations in World Models](https://arxiv.org/abs/2608.22764) | - |
| 2026 | arXiv | LRC-JEPA | [LRC-JEPA: Disentangling Dynamics and Residual Context for Efficient World Models](https://arxiv.org/abs/2609.34375) | - |
| 2026 | arXiv | MA-JEPA | [MA-JEPA: Joint-Embedding World Models for Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.33563) | - |
| 2026 | arXiv | - | [Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning](https://arxiv.org/abs/2611.22483) | - |
| 2026 | arXiv | MDN-VJEPA | [MDN-VJEPA: Multimodal Probabilistic Joint-Embedding World Models](https://arxiv.org/abs/2610.13956) | - |
| 2026 | arXiv | MemWM | [MemWM: Associative Memory-Enhanced Latent World Models for Long-Horizon Planning](https://arxiv.org/abs/2610.19683) | - |
| 2026 | arXiv | Mini-JEPA | [Mini-JEPA Foundation Model Fleet Enables Agentic Hydrologic Intelligence](https://arxiv.org/abs/2605.14120) | - |
| 2026 | arXiv | MORE | [MORE: Learning Motion-Oriented Registers for Driving World Models and Planning](https://arxiv.org/abs/2610.14871) | - |
| 2026 | arXiv | - | [No Gaussian Required: Contrastive Inverse Dynamics for JEPA World Models](https://arxiv.org/abs/2608.17542) | [Code](https://github.com/jackboyla/action-contrastive-jepa) |
| 2026 | arXiv | - | [One Future, Every Robot: Label-Efficient Collective-State Prediction with Decentralized JEPA](https://arxiv.org/abs/2607.28443) | - |
| 2026 | NeurIPS Workshop | - | [One-Step Prediction Fidelity Is a Poor Proxy for Planning Performance in JEPA World Models](https://arxiv.org/abs/2610.19375) | - |
| 2026 | arXiv | Orthogonal JEPA | [Orthogonal JEPA: Factorized Predictive States for Latent World Models](https://arxiv.org/abs/2608.20065) | - |
| 2026 | arXiv | PhyLatent | [PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models](https://arxiv.org/abs/2608.05720) | - |
| 2026 | arXiv | - | [Policy-Guided World Model Planning for Language-Conditioned Visual Navigation](https://arxiv.org/abs/2603.25981) | - |
| 2026 | CIKM | - | [Predict to Generate: Enhancing Diffusion World Models with JEPA-based Latent Dynamics for Traffic Management](https://doi.org/10.1145/3799682.3839934) | - |
| 2026 | CoRL Workshop | - | [Prediction or Persistence? What Future-Prediction Scores Miss About World Models](https://arxiv.org/abs/2611.15082) | - |
| 2026 | arXiv | - | [Predictive Objectives Discard Exogenous Control-Relevant Features: A Controlled Mechanistic Study](https://arxiv.org/abs/2606.30068) | [Code](https://github.com/bushesarebetter/jepa_research_project) |
| 2026 | arXiv | - | [Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models](https://arxiv.org/abs/2610.07540) | - |
| 2026 | arXiv | Qantara | [Qantara: Bridge-Flow Training for Multi-Paradigm JEPA Inference](https://arxiv.org/abs/2607.04978) | [Project](https://corl-team.github.io/qantara) |
| 2026 | arXiv | Quantum-JEPA | [Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models](https://arxiv.org/abs/2610.27921) | - |
| 2026 | arXiv | RAN-JEPA | [RAN-JEPA: An Action-Conditioned World Model for Energy-efficient Mobile Network Control](https://arxiv.org/abs/2610.17584) | - |
| 2026 | arXiv | RD-JEPA | [RD-JEPA: Predictive latent pretraining for few-trajectory transfer across reaction--diffusion equations](https://arxiv.org/abs/2609.29403) | - |
| 2026 | arXiv | Rectified LpJEPA | [Rectified LpJEPA: Joint-Embedding Predictive Architectures with Sparse and Maximum-Entropy Representations](https://arxiv.org/abs/2602.01456) | - |
| 2026 | arXiv | ReLAP | [ReLAP: Latent Action Pretraining through Recurrent Video Prediction in JEPA Space](https://arxiv.org/abs/2611.22077) | - |
| 2026 | IEEE Conference on Games | RePAIR | [RePAIR: Predictive Self-Supervised Representation Learning in Chess](https://arxiv.org/abs/2606.11860) | - |
| 2026 | arXiv | - | [Reperesentation Geometry Matters for Planning with JEPA World Models](https://arxiv.org/abs/2608.16287) | - |
| 2026 | arXiv | - | [Risk-Triggered Search: Behavior-Preserving Safe Control](https://arxiv.org/abs/2611.24409) | - |
| 2026 | arXiv | RoboJEPA | [RoboJEPA: Scaling Robotic Latent World Models](https://arxiv.org/abs/2610.10515) | - |
| 2026 | arXiv | RSI-Anything | [RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://arxiv.org/abs/2610.13912) | [Code](https://github.com/Gen-Verse/RSI-Anything) |
| 2026 | arXiv | SaiVLA-JEPA | [SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control](https://arxiv.org/abs/2610.38508) | - |
| 2026 | International Journal of Science Strategic Management… | - | [Scaling Laws and Architectural Advances of Hierarchical JEPA (H-JEPA) Model for Planning, Control and Robotics in Physical Systems](https://doi.org/10.55041/ijsmt.v2i5.169) | - |
| 2026 | arXiv | - | [Self-Supervised JEPA-based World Models for LiDAR Occupancy Completion and Forecasting](https://arxiv.org/abs/2602.12540) | - |
| 2026 | arXiv | - | [Self-Supervised Latent Action-Conditioned World Modeling for Time Series](https://arxiv.org/abs/2610.37963) | - |
| 2026 | arXiv | Semigroup-JEPA | [Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization](https://arxiv.org/abs/2609.10464) | [Project](https://sg-jepa.github.io) |
| 2026 | arXiv | SJEPA | [SJEPA: Learning Elegant Latent Dynamics with Hybrid Symbolic-Neural Predictors](https://arxiv.org/abs/2608.04060) | - |
| 2026 | arXiv | SkyJEPA | [SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors](https://arxiv.org/abs/2606.23444) | - |
| 2026 | arXiv | Slot-JEPA | [Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models](https://arxiv.org/abs/2610.28074) | - |
| 2026 | arXiv | Sparse-TD-JEPA | [Sparse-TD-JEPA: Improving Zero-Shot Reinforcement Learning With Sparse Latent Task Representations](https://arxiv.org/abs/2610.14400) | - |
| 2026 | arXiv | - | [Spectral-Target Physical Latent Structuring for JEPA-Style World Models](https://arxiv.org/abs/2609.04264) | - |
| 2026 | arXiv | SpikWM | [SpikWM: Efficient End-to-End Spiking World Modeling for Visual Planning](https://arxiv.org/abs/2611.22981) | [Code](https://github.com/ShawnYE618/SpikWM) |
| 2026 | arXiv | SplitJEPA | [SplitJEPA: Learning Invariant and Variant Latent Worlds without Reconstruction](https://arxiv.org/abs/2610.12349) | - |
| 2026 | arXiv | StageWAM | [StageWAM: Joint-Embedding Stage Prediction for World-Action Models in Robot Manipulation](https://arxiv.org/abs/2608.10780) | - |
| 2026 | arXiv | - | [Staircase Policy: Streaming Inference for World-Action Models with Large Action Chunks](https://arxiv.org/abs/2609.36471) | - |
| 2026 | arXiv | STATERA | [STATERA: Hidden Mass Estimation via Zero-Shot Sim-to-Real Kinematics using Frozen Temporal Tubelets](https://arxiv.org/abs/2610.00003) | - |
| 2026 | arXiv | - | [Stuck in Place: Stall Diagnosis and Remedies for JEPA Planners](https://arxiv.org/abs/2611.25415) | [Code](https://github.com/jhlee0619/unstick) |
| 2026 | arXiv | Sub-JEPA | [Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models](https://arxiv.org/abs/2605.09241) | [Code](https://github.com/intcomp/Sub-JEPA) |
| 2026 | arXiv | Subspace-Decomposed JEPAs | [Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models](https://arxiv.org/abs/2605.31111) | - |
| 2026 | arXiv | - | [Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models](https://arxiv.org/abs/2608.27367) | - |
| 2026 | arXiv | SWIM | [SWIM: Learning What Matters from Behaviors for JEPA World Models](https://arxiv.org/abs/2610.36662) | - |
| 2026 | SPIE Unmanned Systems Technology | - | [Tactical survivability through predictive world modeling: a JEPA-based approach for intelligent unmanned systems](https://doi.org/10.1117/12.3115128) | - |
| 2026 | arXiv | Tactile-JEPA | [Tactile-JEPA: Topology-Aware Self-Supervised Representation Learning for Distributed Tactile Sensors](https://arxiv.org/abs/2609.24385) | [Code](https://github.com/E-Kovtun/tactile) |
| 2026 | arXiv | Temporal-Distance JEPA | [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/abs/2607.25337) | [Code](https://github.com/HKBU-KnowComp/Temporal-Distance-JEPA) |
| 2026 | arXiv | - | [The Planning Limits of Latent World Models](https://arxiv.org/abs/2609.39235) | - |
| 2026 | LNCS | Thermo-JEPA | [Thermo-JEPA: Learning a Geometry-Grounded Thermal World Model via Cross-Modal Privileged Masking](https://doi.org/10.1007/978-3-032-37013-6_7) | - |
| 2026 | arXiv | ThinkJEPA | [ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model](https://arxiv.org/abs/2603.22281) | - |
| 2026 | arXiv | Time-JEPA | [Time-JEPA: Grounding Video World Models with Physical Time Series](https://arxiv.org/abs/2610.23982) | [Code](https://github.com/Lishenyi2004/Time-JEPA) |
| 2026 | arXiv | - | [Time-to-Goal: Learned Temporal Metrics for Long-Horizon Planning with JEPA World Models](https://arxiv.org/abs/2611.05847) | - |
| 2026 | arXiv | Touch-JEPA | [Touch-JEPA: Tactile Representation Learning from Hand-Object Video with Limited Tactile Supervision](https://arxiv.org/abs/2610.28519) | [Project](https://touch-jepa.github.io) |
| 2026 | arXiv | - | [Toward Goal-Agnostic Joint-Embedding Predictive Control of Partial Differential Equations](https://arxiv.org/abs/2607.21644) | - |
| 2026 | IROS Workshop | - | [Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planning](https://arxiv.org/abs/2609.03565) | - |
| 2026 | arXiv | TwinJEPA | [TwinJEPA: Action-Preferred Predictive Representations for Goal-Conditioned Control](https://arxiv.org/abs/2610.02922) | - |
| 2026 | arXiv | Underwater C3-JEPA | [Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage](https://arxiv.org/abs/2609.30214) | - |
| 2026 | arXiv | UniJEPA | [UniJEPA: A Unified Joint-Embedding Predictive Architecture for Task-Agnostic Visual World Modeling](https://arxiv.org/abs/2608.07409) | - |
| 2026 | arXiv | V-JEPA Policy | [V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents](https://arxiv.org/abs/2609.37250) | [Project](https://breez3young.github.io/vjepa-policy/) |
| 2026 | arXiv | Vision-Predictor-Action | [Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors](https://arxiv.org/abs/2610.15556) | [Code](https://github.com/ylee-sling/Vision-Predictor-Action) |
| 2026 | arXiv | VJEPA | [VJEPA: Variational Joint Embedding Predictive Architectures as Probabilistic World Models](https://arxiv.org/abs/2601.14354) | - |
| 2026 | ECCV | VLA-JEPA | [VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model](https://arxiv.org/abs/2602.10098) | - |
| 2026 | arXiv | WA-JEPA | [WA-JEPA: Goal-Aware Predictive Feedback Action Refinement for a World-Action Model](https://arxiv.org/abs/2611.19183) | [Code](https://github.com/Dovisya/WA-JEPA) |
| 2026 | arXiv | WARP-JEPA | [WARP-JEPA: World-Model-in-the-Loop Amortized Rollout Planning for Frozen Hierarchical Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2611.10806) | [Code](https://github.com/hideinsewer/WARP-JEPA) |
| 2026 | arXiv | WCM | [WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning](https://arxiv.org/abs/2607.29613) | - |
| 2026 | Preprints.org | WFC-JEPA | [WFC-JEPA: Constrained World Generation via Wave Function Collapse](https://doi.org/10.20944/preprints202610.2899.v1) | - |
| 2026 | SSRN | - | [When Does Cognition Help a World-Model Planner? A Controlled Dissociation, the Reliable-Horizon Condition, and Evidence on a Pretrained Embodied JEPA](https://doi.org/10.2139/ssrn.7046638) | - |
| 2026 | arXiv | WM-Quant | [WM-Quant: Rollout-Aware Post-Training Quantization for JEPA-Style World Models](https://arxiv.org/abs/2611.21882) | - |
| 2026 | arXiv | - | [World Model Interpretability: From Decoding Representations to Understanding Latent Worlds](https://arxiv.org/abs/2610.25296) | - |
| 2026 | arXiv | - | [World Modeling through Spectral Alignment](https://arxiv.org/abs/2610.15429) | - |
| 2026 | LNCS | CA-JEPA | [World Models as Constraints: Heterogeneous Rail Robot Coordination via CA-JEPA and LLM-Based Planning](https://doi.org/10.1007/978-981-92-2014-4_16) | - |
| 2026 | arXiv | - | [Worth Remembering: Surprise-Gated Robot Episodic Memory](https://arxiv.org/abs/2606.03787) | - |
| 2026 | arXiv | τ | [τ: Learning Touch-Augmented Vision-Language-Action Models from Future Visual Supervision](https://arxiv.org/abs/2607.24485) | [Project](https://cocacola-lab.github.io/tau-Page/) |
| 2025 | arXiv | - | [EmbodiSwap for Zero-Shot Robot Imitation Learning](https://arxiv.org/abs/2510.03706) | - |
| 2025 | ESANN | JEPA for RL | [JEPA for RL: Investigating Joint-Embedding Predictive Architectures for Reinforcement Learning](https://arxiv.org/abs/2504.16591) | - |
| 2025 | IFAC-PapersOnLine | - | [Learning State-Space Models of Dynamic Systems from Arbitrary Data using Joint Embedding Predictive Architectures](https://arxiv.org/abs/2508.10489) | - |
| 2025 | ICLR | - | [Learning Video-Conditioned Policy on Unlabelled Data with Joint Embedding Predictive Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/hash/dc9e095f668044e7a0909a4ea3926beb-Abstract-Conference.html) | - |
| 2025 | NeurIPS | seq-JEPA | [seq-JEPA: Autoregressive Predictive Learning of Invariant-Equivariant World Models](https://arxiv.org/abs/2505.03176) | - |
| 2025 | ICLR | TD-JEPA | [TD-JEPA: Latent-predictive Representations for Zero-Shot Reinforcement Learning](https://arxiv.org/abs/2510.00739) | - |
| 2025 | SPIE Pattern Recognition and Prediction | - | [Utilizing V-JEPA for action recognition on the lunar surface: advancing human-robot collaboration](https://doi.org/10.1117/12.3052411) | - |
| 2025 | arXiv | - | [Value-guided action planning with JEPA world models](https://arxiv.org/abs/2601.00844) | - |
| 2025 | TMLR | - | [What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?](https://arxiv.org/abs/2512.24497) | [Code](https://github.com/facebookresearch/jepa-wms) |
| 2024 | J. Stat. Mech | - | [Introduction to Latent Variable Energy-Based Models: A Path Towards Autonomous Machine Intelligence](https://arxiv.org/abs/2306.02572) | - |
| 2022 | NeurIPS Workshop | - | [Joint Embedding Predictive Architectures Focus on Slow Features](https://arxiv.org/abs/2211.10831) | [Code](https://github.com/vladisai/JEPA_SSL_NeurIPS_2022) |

### JEPA-M: Multimodal

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | AC-JEPA | [AC-JEPA: Anchored Cross-Modal Joint Embedding Predictive Architecture for Visual-to-Symbolic Translation](https://arxiv.org/abs/2610.36493) | - |
| 2026 | arXiv | AquaJEPA | [AquaJEPA: An Action-Conditioned Multimodal JEPA Family for Underwater Robot Dynamics](https://arxiv.org/abs/2607.29393) | - |
| 2026 | arXiv | - | [Asymmetric Multimodal Learning with Decomposed JEPAs](https://arxiv.org/abs/2611.16639) | - |
| 2026 | (ARTS)@TALN | - | [Asymmetric Within-Document Predictive Learning for Scientific Document Representation](https://arxiv.org/abs/2608.28625) | - |
| 2026 | arXiv | AV-JEPA | [AV-JEPA: Extending LeJEPA to Audio-Visual Self-Supervised Learning](https://arxiv.org/abs/2607.15295) | - |
| 2026 | BMVC | CAPE-JEPA | [CAPE-JEPA - Cross-modal Adversarial Probabilistic Embedding JEPA](https://arxiv.org/abs/2611.06247) | - |
| 2026 | arXiv | DuoJEPA | [DuoJEPA: Cross-Modal Translation Between Unaligned Self-Supervised Embedding Spaces](https://arxiv.org/abs/2611.15968) | - |
| 2026 | ACL | - | [Latent Prediction Needs Alignment: A Controlled Study of Joint-Embedding Predictive Vision–Language Learning](https://doi.org/10.18653/2026.aacl-long.232) | - |
| 2026 | CVPR Workshop | Le MuMo JEPA | [Le MuMo JEPA: Multi-Modal Self-Supervised Representation Learning with Learnable Fusion Tokens](https://arxiv.org/abs/2603.24327) | - |
| 2026 | arXiv | LeAVJEPA | [LeAVJEPA: A Minimalist Architecture for Audio-Visual Self-Supervised Learning](https://arxiv.org/abs/2610.06226) | - |
| 2026 | arXiv | MacJEPA | [MacJEPA: Missingness-Robust Audio-Visual Recognition from Untrimmed Egocentric Videos](https://arxiv.org/abs/2610.08192) | - |
| 2026 | ECCV | MJEPA | [MJEPA: A Simple and Scalable Joint-Embedding Predictive Architecture for Audio-Visual Learning](https://arxiv.org/abs/2606.25225) | - |
| 2026 | arXiv | - | [Multimodal Latent Reasoning via Predictive Embeddings](https://arxiv.org/abs/2604.08065) | - |
| 2026 | arXiv | - | [Predictive Associative Memory: Retrieval Beyond Similarity Through Temporal Co-occurrence](https://arxiv.org/abs/2602.11322) | [Code](https://github.com/EridosAI/PAM-Benchmark) |
| 2026 | arXiv | - | [Text-Conditional JEPA for Learning Semantically Rich Visual Representations](https://arxiv.org/abs/2605.03245) | - |
| 2026 | arXiv | UMM-JEPA | [UMM-JEPA: Generative Pretraining via Masked Next-Scale Representation Prediction for Unified Multimodal Models](https://arxiv.org/abs/2611.18668) | - |
| 2026 | arXiv | V-JEPA-LM | [V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations](https://arxiv.org/abs/2611.17831) | [Code](https://github.com/kkt94/Llama-V-JEPA-LM) |
| 2026 | International Conference on Image, Vision and Computing | VL-JEPA | [VL-JEPA World Model with Energy-Based Scoring for Feeding Behavior Detection in Pangasianodon hypophthalmus](https://doi.org/10.1109/icivc70586.2026.11686614) | - |
| 2025 | arXiv | JEPA-T | [JEPA-T: Joint-Embedding Predictive Architecture with Text Fusion for Image Generation](https://arxiv.org/abs/2510.00974) | [Code](https://github.com/justin-herry/JEPA-T.git) |
| 2025 | arXiv | - | [Seeing Beyond Words: Self-Supervised Visual Learning for Multimodal Large Language Models](https://arxiv.org/abs/2512.15885) | [Code](https://github.com/aimagelab/JARVIS) |
| 2025 | arXiv | TI-JEPA | [TI-JEPA: An Innovative Energy-based Joint Embedding Strategy for Text-Image Multimodal Systems](https://arxiv.org/abs/2503.06380) | - |
| 2025 | ICLR | VL-JEPA | [VL-JEPA: Joint Embedding Predictive Architecture for Vision-language](https://arxiv.org/abs/2512.10942) | - |
| 2024 | arXiv | M3-JEPA | [M3-JEPA: Multimodal Alignment via Multi-gate MoE based on the Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2409.05929) | - |
| 2024 | User Modeling, Adaptation, and Personalization | UI-JEPA | [UI-JEPA: Towards Active Perception of User Intent through Onscreen User Activity](https://arxiv.org/abs/2409.04081) | - |

### JEPA-SC: 3D, Structured and Object-Centric

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | 4DGS-JEPA | [4DGS-JEPA: Temporally Compositional Joint-Embedding Prediction for Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.25036) | - |
| 2026 | IEEE Access | AHA-JEPA | [AHA-JEPA: Articulated Hand-Aware JEPA for Leak-Free Gloss-Conditioned Sign Pose Generation](https://doi.org/10.1109/access.2026.3716809) | - |
| 2026 | arXiv | Akasha 2 | [Akasha 2: Hamiltonian State Space Duality and Visual-Language Joint Embedding Predictive Architectur](https://arxiv.org/abs/2601.06212) | - |
| 2026 | HAL | TAP-JEPA | [Balancing Local Geometry and Global Semantics in 3D Point Clouds with TAP-JEPA](https://hal.science/hal-05643766v1) | - |
| 2026 | arXiv | CascadeJEPA | [CascadeJEPA: Enhancing 3D Geometric Representations via Spatially Coupled Cascaded Prediction](https://arxiv.org/abs/2611.22686) | - |
| 2026 | ICML | Causal-JEPA | [Causal-JEPA: Learning World Models through Object-Level Latent Masking](https://arxiv.org/abs/2602.11389) | [Code](https://github.com/galilai-group/cjepa) |
| 2026 | arXiv | Cross4D-JEPA | [Cross4D-JEPA: Dense Cross-modal Correspondence Distillation for 4D Point Cloud Representation Learning](https://arxiv.org/abs/2607.00514) | - |
| 2026 | arXiv | - | [Gaussian-Constrained LeJEPA Representations for Unsupervised Scene Discovery and Pose Consistency](https://arxiv.org/abs/2602.07016) | - |
| 2026 | arXiv | Gaussian-JEPA | [Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats](https://arxiv.org/abs/2608.15651) | [Project](https://amazingren.github.io/Gaussian-JEPA/) |
| 2026 | Mathematics | JEPADepth | [JEPADepth: Masked Predictive Representation Learning for Self-Supervised Monocular Depth Estimation](https://arxiv.org/abs/2607.26600) | - |
| 2026 | arXiv | - | [Joint-Embedding Prediction of Masked Point Tubes for Self-Supervised Learning on 4D Point Cloud Videos](https://arxiv.org/abs/2608.24093) | - |
| 2026 | HAL | LF-JEPA | [LF-JEPA: LEARNING GEOMETRIC REPRESENTATIONS FROM LIGHT FIELDS](https://hal.science/hal-05802104v1) | - |
| 2026 | arXiv | - | [Multi-View 3D Reconstruction Using V-JEPA Features](https://arxiv.org/abs/2611.15143) | [Code](https://github.com/Anwarshamim01/multi-view-3d-reconstruction-using-v-jepa-features) |
| 2026 | LNCS | Path-JEPA | [Path-JEPA: Path Signature Based Predictive Learning for Skeleton Action Recognition](https://doi.org/10.1007/978-3-032-37258-1_7) | - |
| 2026 | Automation in Construction | - | [Self-supervised learning for BIM element classification using a joint embedding predictive architecture](https://doi.org/10.1016/j.autcon.2026.107075) | - |
| 2026 | International Conference on Control and Automation | - | [Self-Supervised LiDAR-Camera Fusion with Joint Embedding Predictive Architecture for 3D Object Detection](https://doi.org/10.1109/icca69928.2026.11618227) | - |
| 2026 | arXiv | SR-JEPA | [SR-JEPA: Learning Predictive Latent State in 3D Scenes](https://arxiv.org/abs/2608.05774) | - |
| 2026 | Automation in Construction | - | [Toward generalizable foundation models for 3D BIM geometry using a joint embedding predictive architecture](https://doi.org/10.1016/j.autcon.2026.107169) | - |
| 2025 | arXiv | CrossJEPA | [CrossJEPA: Cross-Modal Joint-Embedding Predictive Architecture for Efficient 3D Representation Learning from 2D Images](https://arxiv.org/abs/2511.18424) | - |
| 2025 | arXiv | Point-JEPA | [Label-Efficient Grasp Joint Prediction with Point-JEPA](https://arxiv.org/abs/2509.13349) | - |
| 2025 | CVPR | POMA-3D | [POMA-3D: The Point Map Way to 3D Scene Understanding](https://arxiv.org/abs/2511.16567) | [Project](https://matchlab-imperial.github.io/poma3d/) |
| 2024 | arXiv | 3D-JEPA | [3D-JEPA: A Joint Embedding Predictive Architecture for 3D Self-Supervised Representation Learning](https://arxiv.org/abs/2409.15803) | - |
| 2024 | WACV Workshop | Point-JEPA | [Point-JEPA: A Joint Embedding Predictive Architecture for Self-Supervised Learning on Point Cloud](https://arxiv.org/abs/2404.16432) | - |
| 2024 | LNCS | S-JEPA | [S-JEPA: A Joint Embedding Predictive Architecture for Skeletal Action Recognition](https://doi.org/10.1007/978-3-031-73411-3_21) | - |

## Applications

### Autonomous Driving

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | AD-E2E-JEPA | [AD-E2E-JEPA: A Joint-Embedding Predictive Architecture For End-to-End Autonomous Driving](https://arxiv.org/abs/2609.34085) | [Code](https://github.com/HaoranZhuExplorer/AD-E2E-JEPA) |
| 2026 | arXiv | - | [Asleep at the Wheel: JEPA's Limitations in Evaluating Novel Driving Data](https://arxiv.org/abs/2608.01336) | - |
| 2026 | arXiv | Auto-JEPA | [Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.29031) | - |
| 2026 | NeurIPS | - | [Drive vs. Decay: On the Training Dynamics of Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2610.02344) | [Code](https://github.com/jose-melo/drive-vs-decay) |
| 2026 | arXiv | Drive-JEPA | [Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving](https://arxiv.org/abs/2601.22032) | - |
| 2026 | International Conference on Intelligent Information… | EBM-JEPA-Drive | [EBM-JEPA-Drive: Energy-Based World Models for Autonomous Driving via Joint Embedding Predictive Architectures](https://doi.org/10.1145/3805862.3805904) | - |
| 2026 | arXiv | - | [Geographic Diversity Beats Data Volume for Cross-Domain Generalization in Zero-Label JEPA Driving World Models](https://arxiv.org/abs/2607.04500) | - |
| 2026 | ECCV Workshop | JEPA Guided Diffusion | [JEPA Guided Diffusion: Predictive Vision-Language Conditioning for Generative Traffic Forecasting](https://arxiv.org/abs/2609.21379) | - |
| 2026 | Defence Technology | - | [JEPA-based multimodal trajectory prediction for air targets in complex electromagnetic environments](https://doi.org/10.1016/j.dt.2026.06.008) | - |
| 2026 | arXiv | - | [Mask What Matters: Saliency-Guided Video Self-Supervised Learning for Autonomous Driving](https://arxiv.org/abs/2608.17178) | - |
| 2026 | International Conference on Parallel Architectures and… | - | [Mask-Aware Execution for Efficient JEPA Training](https://arxiv.org/abs/2609.22674) | - |
| 2026 | Sensors | LM-JEPA | [Object Detection and Scene Perception for Connected and Autonomous Vehicles Using LM-JEPA](https://doi.org/10.3390/s26154894) | - |
| 2026 | arXiv | - | [Predictive Closure: A Set-Level Characterization of JEPA's Feature Selection](https://arxiv.org/abs/2610.27364) | - |
| 2026 | ECCV | - | [Sim-to-Real Traffic Scene Understanding by Decoupling Semantics from Caption Generation with V-JEPA](https://arxiv.org/abs/2609.18562) | - |
| 2026 | ICC | - | [Spatiotemporal Semantic V2X Framework for Cooperative Collision Prediction](https://arxiv.org/abs/2601.17216) | - |
| 2026 | International Conference on Advanced Electronic… | TrajJEPA | [TrajJEPA: A Joint-Embedding Predictive Model For Multi-agent Trajectory Prediction](https://doi.org/10.1109/aetcse69203.2026.11504088) | - |
| 2026 | International Conference on Image, Vision and Computing | V-JEPA-Drive | [V-JEPA-Drive: Uncertainty-Aware Self-Supervised Predictive Learning for Multi-Camera Autonomous Driving Perception](https://doi.org/10.1109/icivc70586.2026.11686495) | - |
| 2026 | IoT-J | V2X-JEPA | [V2X-JEPA: Self-Supervised Multiagent Joint Embedding Predictive Architecture for Robust Vehicle-to-Everything Perception](https://doi.org/10.1109/jiot.2026.3660030) | - |
| 2026 | arXiv | WA-JEPA | [WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving](https://arxiv.org/abs/2608.20974) | [Code](https://github.com/AFARI-Research/WA-JEPA) |
| 2026 | Translational Data Science for Social Impact | - | [Who Is Seen in Time? Timely-Warning Opportunity and a Partial Equity Audit of a V-JEPA-Enhanced Pedestrian Warning System](https://doi.org/10.1177/27556662261493621) | - |
| 2026 | arXiv | World4Scorer | [World4Scorer: Outcome-Grounded World Modeling for Autonomous Driving](https://arxiv.org/abs/2609.36438) | [Project](https://guobapei.github.io/World4Scorer/) |
| 2026 | arXiv | WTR-Drive | [WTR-Drive: World-Task Decomposition with Structured Risk Supervision for End-to-End Driving](https://arxiv.org/abs/2611.20510) | - |
| 2026 | arXiv | - | [Zero-Label Driving Scenario Complexity Detection via Joint Embedding Predictive Architecture](https://arxiv.org/abs/2606.28383) | - |
| 2025 | AAAI | - | [Self-Supervised Representation Learning with Joint Embedding Predictive Architecture for Automotive LiDAR Object Detection](https://arxiv.org/abs/2501.04969) | - |

### Medical and Healthcare

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2027 | WACV | MADJEPA | [MADJEPA: Enhanced Multi-Stage Joint-Embedding Predictive Architecture for Medical Anomaly Detection](https://arxiv.org/abs/2611.25194) | [Code](https://github.com/Sabina085/madjepa) |
| 2026 | SLEEP | 0359 Sleep-JEPA | [0359 Sleep-JEPA: Joint Embedding Representations of Sleep Study Data Accurately Estimate Sleep Features and Long-Term Health Outcomes](https://doi.org/10.1093/sleep/zsag091.0359) | - |
| 2026 | arXiv | - | [A Framework for Early Sepsis Prediction via Self-Supervised (JEPA) and Federated Representation Learning](https://arxiv.org/abs/2607.16681) | - |
| 2026 | arXiv | - | [A Hybrid CNN--State-Space--Attention Backbone with Joint-Embedding Predictive Pretraining for 12-Lead ECG Classification](https://arxiv.org/abs/2609.29376) | [Code](https://github.com/yakoubbazi/Hybrid_ECG_Jepa) |
| 2026 | arXiv | AEGIS | [AEGIS: A Multi-Task Joint-Embedding Predictive Architecture for Mammography](https://arxiv.org/abs/2607.00277) | - |
| 2026 | arXiv | AG-JEPA | [AG-JEPA: Anatomically Guided Joint Embedding Predictive Architecture for Neurodegenerative Representation Learning](https://arxiv.org/abs/2611.18097) | - |
| 2026 | arXiv | - | [Are Joint-Embedding Predictive Objectives Effective for Longitudinal EHRs?](https://arxiv.org/abs/2610.29528) | - |
| 2026 | arXiv | Arti-JEPA | [Arti-JEPA: Adapting Video World Model to Real-Time MRI of the Vocal Tract for Speech-Production Analysis](https://arxiv.org/abs/2609.09757) | - |
| 2026 | JMIR Medical Informatics | - | [Artificial Intelligence Models for Predicting Triage in Emergency Departments: Seven-Month Retrospective Comparative Study of Natural Language Processing, Large Language Model, and Joint Embedding Predictive Architectures](https://doi.org/10.2196/83318) | - |
| 2026 | arXiv | BAC-JEPA | [BAC-JEPA: Label-Efficient Breast Arterial Calcification Segmentation via Synthetic Mammography-Guided Supervision](https://arxiv.org/abs/2606.22089) | - |
| 2026 | arXiv | - | [Beyond Patient Invariance: Learning Cardiac Dynamics via Action-Conditioned JEPAs](https://arxiv.org/abs/2604.22618) | [Code](https://github.com/cljosegfer/lesaude-dynamics) |
| 2026 | arXiv | - | [Beyond Representation Learning: A Systematic Study of Joint-Embedding Predictive Generation for 3D Brain MRI](https://arxiv.org/abs/2608.28787) | - |
| 2026 | arXiv | CardioState-JEPA | [CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation](https://arxiv.org/abs/2608.12944) | - |
| 2026 | arXiv | CGM-JEPA | [CGM-JEPA: Learning Consistent Continuous Glucose Monitor Representations via Predictive Self-Supervised Pretraining](https://arxiv.org/abs/2605.00933) | [Code](https://github.com/cruiseresearchgroup/CGM-JEPA) |
| 2026 | arXiv | Clin-JEPA | [Clin-JEPA: A Multi-Phase Co-Training Framework for Joint-Embedding Predictive Pretraining on EHR Patient Trajectories](https://arxiv.org/abs/2605.10840) | [Code](https://github.com/Kamaleswaran-Lab/Clin-JEPA) |
| 2026 | arXiv | Clinical Graph-JEPA | [Clinical Graph-JEPA: Predictive Patient-State Knowledge Graphs for Cognitive Decision Support](https://arxiv.org/abs/2608.22583) | - |
| 2026 | arXiv | - | [Contrastive Joint-Embedding Prediction for Representation Learning in Structural MRI](https://arxiv.org/abs/2607.11962) | - |
| 2026 | arXiv | - | [Cracks in Embeddings: Robustness and Stability of JEPA-Based Chest X-Ray Representations](https://arxiv.org/abs/2611.17905) | - |
| 2026 | arXiv | - | [Cross-Modal Ultrasound-MRI Learning for Fetal Brain Ventricular Volumetry and Abnormality Screening](https://arxiv.org/abs/2608.14763) | - |
| 2026 | arXiv | - | [Curriculum-Driven 3D CT Report Generation via Language-Free Visual Grafting and Zone-Constrained Compression](https://arxiv.org/abs/2603.23308) | - |
| 2026 | arXiv | DALE-CT | [DALE-CT: Depth-Aware 2D Slice Encoders Learn an Anatomical World Model of Chest CT](https://arxiv.org/abs/2606.07775) | - |
| 2026 | NeurIPS Workshop | DES-JEPA | [DES-JEPA: Learning a Shared Vocabulary for High-Dimensional Discrete Event Sequences](https://arxiv.org/abs/2610.38445) | - |
| 2026 | arXiv | EchoJEPA | [EchoJEPA: A Latent Predictive Foundation Model for Echocardiography](https://arxiv.org/abs/2602.02603) | - |
| 2026 | arXiv | EEG-JEPA | [EEG-JEPA: Structured Latent Prediction for EEG Foundation Models](https://arxiv.org/abs/2608.00114) | - |
| 2026 | arXiv | EndoWorld-JEPA | [EndoWorld-JEPA: Motion-Guided Global-Local Latent World Modeling for Endoscopic Video Representation Learning](https://arxiv.org/abs/2610.27890) | - |
| 2026 | LNCS | FetalHeart AI | [FetalHeart AI: A Dual-Architecture Self-supervised Learning Framework Using I-JEPA and V-JEPA 2 for Congenital Heart Disease Detection in Fetal Ultrasound](https://doi.org/10.1007/978-981-92-2891-1_17) | - |
| 2026 | ECCV | FlexiBrain | [FlexiBrain: Resolution-Agnostic Voxel-Level Encoding for Native fMRI](https://arxiv.org/abs/2606.11500) | [Code](https://github.com/OneMore1/FlexiBrain) |
| 2026 | International Conference on Intelligent Information… | H-Seg-JEPA | [H-Seg-JEPA: Hierarchical Joint-Embedding Predictive Architecture for Multi-Scale Medical Image Segmentation](https://doi.org/10.1145/3805862.3805932) | - |
| 2026 | arXiv | IQ-JEPA | [IQ-JEPA: A Joint-Embedding Predictive Architecture with a Hermitian Vision Transformer for Sound Speed and Attenuation Estimation from Ultrasound IQ Data](https://arxiv.org/abs/2607.22351) | - |
| 2026 | arXiv | JEPA-Anything | [JEPA-Anything: Learning Predictive Models across Different Worlds](https://arxiv.org/abs/2609.20800) | [Code](https://github.com/Gen-Verse/JEPA-Anything) |
| 2026 | Biomedical Engineering Letters | JEPA-Mamba | [JEPA-Mamba: a self-supervised joint-embedding architecture with bidirectional Mamba for ECG representation learning](https://doi.org/10.1007/s13534-026-00620-w) | - |
| 2026 | International Conference on Image, Vision and Computing | - | [Joint-Embedding Predictive Pretraining for Energy-Calibrated Skin Cancer Screening](https://doi.org/10.1109/icivc70586.2026.11686580) | - |
| 2026 | arXiv | - | [Latent Prediction Yields Cross-Subject Alignable Representations in Sensory-Evoked fMRI](https://arxiv.org/abs/2610.40280) | - |
| 2026 | arXiv | Laya | [Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstruction](https://arxiv.org/abs/2603.16281) | - |
| 2026 | Biomedical informatics | LC-JEPA | [LC-JEPA: a logic-constrained self-supervised framework for trustworthy ECG arrhythmia analysis](https://doi.org/10.55092/bi20260001) | - |
| 2026 | Neural Networks | - | [Learning General Representation of 12-Lead Electrocardiogram with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2410.08559) | [Code](https://github.com/sehunfromdaegu/ECG_JEPA) |
| 2026 | arXiv | - | [Learning Multimodal Sensor Fusion with JEPA Representations for Breathing Activity and Pose Recognition](https://arxiv.org/abs/2610.15891) | - |
| 2026 | arXiv | - | [Learning Sparse Latent Predictive Foundation Model for Multimodal Neuroimaging](https://arxiv.org/abs/2606.14957) | - |
| 2026 | arXiv | - | [Masked and Predictive Self-Supervised Pretraining for Brain MRI: Effects of Objective Design on Disease Detection](https://arxiv.org/abs/2606.13315) | - |
| 2026 | arXiv | MeFEm | [MeFEm: Medical Face Embedding model](https://arxiv.org/abs/2602.14672) | [Code](https://huggingface.co/boretsyury/MeFEm) |
| 2026 | AAAI | mmJEPA-ECG | [mmJEPA-ECG: Cross-Posture Robust Contactless Electrocardiogram Monitoring via Millimeter Wave Radar Sensing](https://doi.org/10.1609/aaai.v40i45.41242) | - |
| 2026 | MICCAI Workshop | MR-JEPA | [MR-JEPA: A General Purpose Video Foundation Model for Cardiac MRI](https://arxiv.org/abs/2608.30975) | - |
| 2026 | Research Square | Neuro-JEPA | [Neuro-JEPA: Building and Evaluating Health-System Scale Neuroimaging Foundation Models with Mixture of Experts](https://doi.org/10.21203/rs.3.rs-11130462/v1) | - |
| 2026 | arXiv | OmniRAS | [OmniRAS: Standardizing Foundation Model Training and Evaluation in Robot-Assisted Surgery](https://arxiv.org/abs/2608.31048) | - |
| 2026 | bioRxiv | Panvascular-JEPA | [Panvascular-JEPA: Unseen-Structure Evaluation of Factorized Predictive States for Hemodynamic Networks](https://doi.org/10.64898/2026.10.12.758273) | - |
| 2026 | arXiv | - | [Patient, Place, Prior (P$^3$): What Counts as Personalization in Medical World Models?](https://arxiv.org/abs/2610.09194) | - |
| 2026 | International Conference on Neural Networks and… | Physio-JEPA | [Physio-JEPA for ICU Signals: Temporal Multimodal Explainability and the Temporal Range Coherence Metric for Ventricular Tachycardia Alarm Validation](https://doi.org/10.1109/neuront71829.2026.11650778) | - |
| 2026 | arXiv | ProtoCouncil | [ProtoCouncil: Multi-Encoder Anatomical Prototypes for Prostate Cancer Detection in Micro-Ultrasound](https://arxiv.org/abs/2611.09058) | - |
| 2026 | arXiv | Rad-JEPA 3D | [Rad-JEPA 3D: Radiology Joint-Embedding Predictive Model for 3D Computed Tomography](https://arxiv.org/abs/2607.26196) | - |
| 2026 | EMNLP | RadJEPA | [RadJEPA: Radiology Encoder for Chest X-Rays via Joint Embedding Predictive Architecture](https://arxiv.org/abs/2601.15891) | - |
| 2026 | arXiv | - | [Rhythm-Structured Predictive Learning for Remote Photoplethysmography](https://arxiv.org/abs/2606.31736) | [Code](https://github.com/deconasser/RhythmJEPA) |
| 2026 | arXiv | - | [Scaling Video Pretraining for Surgical Foundation Models](https://arxiv.org/abs/2603.29966) | - |
| 2026 | CCIS | Seg-JEPA | [Seg-JEPA: Joint-Embedding Predictive Architecture for Self-Supervised Medical Image Segmentation](https://doi.org/10.1007/978-981-92-0068-9_7) | - |
| 2026 | arXiv | - | [Self-supervised DXA representations encode multi-system disease risk, biological aging and heritability](https://arxiv.org/abs/2608.02208) | - |
| 2026 | CCIS | - | [Self-supervised ViT for Endoscopy: I-JEPA Pretraining with Label-Free Diffusion Assessment](https://doi.org/10.1007/978-981-92-2600-9_2) | - |
| 2026 | medRxiv | SleepJEPA | [SleepJEPA: Learning the latent world of sleep with at-home sleep data to estimate disease risk](https://doi.org/10.64898/2026.03.20.26348834) | - |
| 2026 | NeurIPS | SPERA | [SPERA: Spherical Prior EEG Foundation Model with Geometry- and Frequency-Aware Latent Prediction](https://arxiv.org/abs/2610.10571) | - |
| 2026 | arXiv | STST-JEPA | [STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture For EEG Self-Supervised Learning](https://arxiv.org/abs/2607.06629) | - |
| 2026 | arXiv | - | [The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR](https://arxiv.org/abs/2601.22128) | [Code](https://huggingface.co/standardmodelbio/SMB-v1-1.7B-Structure) |
| 2026 | arXiv | - | [The Predictability Bias of Joint-Embedding Predictive Learning in Medical Imaging](https://arxiv.org/abs/2610.13237) | - |
| 2026 | arXiv | US-JEPA | [US-JEPA: A Joint Embedding Predictive Architecture for Ultrasound](https://arxiv.org/abs/2602.19322) | - |
| 2026 | LNCS | - | [V-JEPA 2 as Temporal World Model for Fetal Cardiac Rhythm Disorder Detection in Ultrasound](https://doi.org/10.1007/978-981-92-5870-3_2) | - |
| 2026 | arXiv | - | [What masking geometry works best for EEG foundation models?](https://arxiv.org/abs/2609.33487) | [Project](https://pierregtch.github.io/eeg-fm-masking) |
| 2026 | NeurIPS Workshop | - | [Where to Predict in Retinal OCT? Anatomy-Guided Target Selection for I-JEPA](https://arxiv.org/abs/2611.17586) | - |
| 2026 | arXiv | - | [Which Pretext Task Transfers? Self-Supervised Pretraining Objectives for Lung Ultrasound](https://arxiv.org/abs/2609.16551) | [Code](https://github.com/moeinheidari7829/LUSVideoSSL) |
| 2026 | HAL | - | [Wiring the Fly Brain into a Hierarchical World Model A self-supervised JEPA world model of a complete connectome Team Piaget: A self-supervised JEPA world model of a complete connectome](https://hal.science/hal-05674559v1) | - |
| 2026 | arXiv | - | [Wrong Organ, Right Physics: Transferring Echocardiography Pretraining to Lung Ultrasound for Tuberculosis Screening](https://arxiv.org/abs/2610.03290) | - |
| 2025 | BDCAT | - | [Development and Comparative Evaluation of Three Artificial Intelligence Models (NLP, LLM, JEPA) for Predicting Triage in Emergency Departments: A 7-Month Retrospective Proof-of-Concept](https://arxiv.org/abs/2507.01080) | - |
| 2025 | arXiv | - | [From Video to EEG: Adapting Joint Embedding Predictive Architecture to Uncover Saptiotemporal Dynamics in Brain Signal Analysis](https://arxiv.org/abs/2507.03633) | - |
| 2025 | MICCAI | - | [Leveraging Generic Foundation Models for Multimodal Surgical Data Analysis](https://arxiv.org/abs/2509.06831) | [Code](https://github.com/DigitalSurgeryLab-Basel/ML-CDS-2025) |
| 2025 | PubMed | PhysioJEPA | [PhysioJEPA: Joint Embedding Representations of Physiological Signals for Real Time Risk Estimation in the Intensive Care Unit.](https://pubmed.ncbi.nlm.nih.gov/42109521) | - |
| 2025 | arXiv | - | [Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture](https://arxiv.org/abs/2509.15470) | - |
| 2025 | Medical Imaging | - | [Self-Supervised Ultrasound-Video Segmentation with Feature Prediction and 3D Localised Loss](https://arxiv.org/abs/2507.18424) | - |
| 2024 | NeurIPS | Brain-JEPA | [Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking](https://arxiv.org/abs/2409.19407) | - |
| 2024 | arXiv | - | [Joint-Embedding Masked Autoencoder for Self-supervised Learning of Dynamic Functional Connectivity from the Human Brain](https://arxiv.org/abs/2403.06432) | - |
| 2024 | Graz Brain-Computer Interface Conference | S-JEPA | [S-JEPA: towards seamless cross-dataset transfer through dynamic spatial attention](https://arxiv.org/abs/2403.11772) | - |
| 2024 | Comput. Biol. Medicine | - | [Self-Supervised Pre-Training with Joint-Embedding Predictive Architecture Boosts ECG Classification Performance](https://arxiv.org/abs/2410.13867) | - |
| 2024 | LNCS | SWJEPA | [SWJEPA: Improving Prostate Cancer Lesion Detection with Shear Wave Elastography and Joint Embedding Predictive Architectures](https://doi.org/10.1007/978-3-031-78398-2_24) | - |

### Scientific Domains

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | AeroJEPA | [AeroJEPA: Learning Semantic Latent Representations for Scalable 3D Aerodynamic Field Modeling](https://arxiv.org/abs/2605.05586) | - |
| 2026 | arXiv | Atom-JEPA | [Atom-JEPA: Joint-Embedding Predictive Architecture for 3D Atomistic Systems](https://arxiv.org/abs/2610.08400) | [Code](https://github.com/khelverskovp/atom-jepa) |
| 2026 | arXiv | Cell-JEPA | [Cell-JEPA: Latent Representation Learning for Single-Cell Transcriptomics](https://arxiv.org/abs/2602.02093) | - |
| 2026 | arXiv | - | [Cross-attention encoding models reveal dynamic spatiotemporal routing across human higher visual cortex](https://arxiv.org/abs/2609.36366) | - |
| 2026 | ICLR | CryoLVM | [CryoLVM: Self-supervised Learning from Cryo-EM Density Maps with Large Vision Models](https://arxiv.org/abs/2602.02620) | - |
| 2026 | arXiv | Crys-JEPA | [Crys-JEPA: Accelerating Crystal Discovery via Embedding Screening and Generative Refinement](https://arxiv.org/abs/2605.14759) | - |
| 2026 | arXiv | D-JEPA | [D-JEPA: Design-Recoverable JEPA Representation with Swappable Physics Decoders](https://arxiv.org/abs/2609.33110) | - |
| 2026 | arXiv | - | [Domain-Informed Multi-View Self-Distillation for Astronomical Light-Curve Representation Learning with JEPA](https://arxiv.org/abs/2606.28446) | - |
| 2026 | bioRxiv | - | [From nucleotides to semantics: genomic representation learning via joint-embedding predictive architecture](https://doi.org/10.64898/2026.04.02.716255) | - |
| 2026 | arXiv | - | [Graph-structured joint-embedding prediction for single-cell transcriptomics](https://arxiv.org/abs/2608.05928) | - |
| 2026 | bioRxiv | HI-JEPA | [HI-JEPA: A World Model of Molecular Organization Learned from Measured Proximity](https://doi.org/10.64898/2026.08.14.744901) | - |
| 2026 | arXiv | - | [HPC-Enabled Video-based Coastal Wave Parameter Estimation Using V-JEPA and Deep Spatiotemporal Learning](https://arxiv.org/abs/2607.11998) | - |
| 2026 | bioRxiv | Hō‘ike | [Hō‘ike: A Joint-Embedding Predictive Architecture for Transcriptome Data Generation with Diffusion Models](https://doi.org/10.64898/2026.08.03.741845) | - |
| 2026 | arXiv | IsoAlign | [IsoAlign: Isoform-Aware DNA-Protein Alignment via Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2611.00241) | - |
| 2026 | arXiv | JEPA for astronomy | [JEPA for astronomy: multi-survey spectral alignment puts stellar parameters on the leading principal axes](https://arxiv.org/abs/2611.23492) | - |
| 2026 | arXiv | JEPA-CFM | [JEPA-CFM: A Joint Embedding Predictive Architecture-based Channel Foundation Model for Robust Fluid Antenna Systems](https://arxiv.org/abs/2607.20202) | - |
| 2026 | arXiv | JEPA-DNA | [JEPA-DNA: Grounding Genomic Foundation Models through Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2602.17162) | - |
| 2026 | arXiv | JetParticle-JEPA | [JetParticle-JEPA: An Efficient Self-Supervised Representation Learning method for Jet Tagging in High-Energy Physics](https://arxiv.org/abs/2606.14813) | - |
| 2026 | bioRxiv | Kūkulu | [Kūkulu: Diffusion-Based Reconstruction of Antibody CDR Loops using a Structure-Aware Joint Embedding Predictive Architecture](https://doi.org/10.64898/2026.08.03.742168) | - |
| 2026 | arXiv | Latent JEPA | [Latent JEPA: Abstract Future Prediction for Latent Reasoning in Chemistry](https://arxiv.org/abs/2610.01947) | - |
| 2026 | arXiv | - | [Learning Radio Astronomical Representations with LeJEPA and Very Small Models](https://arxiv.org/abs/2608.30594) | - |
| 2026 | J. Chem. Inf. Model | M-JEPA | [M-JEPA: Predictive Self-Supervised Learning for Molecular Graphs with Scaffold-Shift Evaluation on Tox21](https://arxiv.org/abs/2610.25163) | - |
| 2026 | arXiv | Mol-JEPA | [Mol-JEPA: A multimodal Joint Embedding Predictive Architecture for Molecules](https://arxiv.org/abs/2608.22642) | - |
| 2026 | arXiv | ScaleAware-JEPA | [Morphological Identification of Dynamical Regimes in MHD Turbulence with ScaleAware-JEPA](https://arxiv.org/abs/2609.36833) | - |
| 2026 | arXiv | - | [Neural Voxel Dynamics: Learning Volumetric Feature Advection for 3D Physics in V-JEPA Latent Space](https://arxiv.org/abs/2606.26410) | [Project](https://wangzican.github.io/publication/nvd/) |
| 2026 | arXiv | NeuroLens | [NeuroLens: Learning Latent Embeddings of Neural Semantics from Chronic Recordings](https://arxiv.org/abs/2610.02864) | - |
| 2026 | arXiv | PDE-JEPA | [PDE-JEPA: Predictive Representation Learning of Latent Dynamics Modeling for Parametric PDEs](https://arxiv.org/abs/2609.34715) | [Project](https://tanpig-x.github.io/PDE-JEPA/) |
| 2026 | arXiv | PerturbJEPA | [PerturbJEPA: Joint-Embedding Predictive Learning of Cellular Perturbation Responses](https://arxiv.org/abs/2611.20575) | [Code](https://github.com/BGI-Hangzhou-OmicsAI/PerturbJEPA) |
| 2026 | arXiv | PI-JEPA | [PI-JEPA: Label-Free Surrogate Pretraining for Coupled Multiphysics Simulation via Operator-Split Latent Prediction](https://arxiv.org/abs/2604.01349) | - |
| 2026 | arXiv | PrecipJEPA | [PrecipJEPA: JEPA-Regularized Future-State Prediction with Motion-Source Rendering for Precipitation Nowcasting](https://arxiv.org/abs/2609.38926) | - |
| 2026 | arXiv | - | [Probing the Latent World: Emergent Discrete Symbols and Physical Structure in Latent Representations](https://arxiv.org/abs/2603.20327) | [Code](https://github.com/cyrilliu1974/JEPA) |
| 2026 | arXiv | ProteinJEPA | [ProteinJEPA: Latent prediction improves protein language model pretraining](https://arxiv.org/abs/2605.07554) | - |
| 2026 | bioRxiv | ProtJEPA | [ProtJEPA: A Multimodal Joint-Embedding Predictive Architecture for Protein Biological World Modeling with Multi-Teacher Modality-Attentive Fusion](https://doi.org/10.64898/2026.08.03.742606) | - |
| 2026 | arXiv | S2S-JEPA | [S2S-JEPA: Predicting the Predictable at Subseasonal-to-Seasonal Timescales](https://arxiv.org/abs/2610.03106) | - |
| 2026 | arXiv | ScaleAware-JEPA | [ScaleAware-JEPA: Latent Representation for Discovery in Multiscale Physical Fields](https://arxiv.org/abs/2606.29723) | [Code](https://github.com/gxli/SA-JEPA) |
| 2026 | arXiv | SuperJEPA | [SuperJEPA: Pretraining with a Supervision-Augmented Joint-Embedding Predictive Architecture for High Energy Physics](https://arxiv.org/abs/2610.36121) | - |
| 2026 | arXiv | - | [Tracing the Unlabeled Storm: Cross-Variable Transfer in a Lagrangian Atmospheric JEPA Framework](https://arxiv.org/abs/2608.22358) | - |
| 2026 | arXiv | - | [Weight-Space Physics: Interpretable Hypernetworks for Lattice Quantum Field Theories](https://arxiv.org/abs/2607.07127) | - |
| 2025 | bioRxiv | GeneJepa | [GeneJepa: A Predictive World Model of the Transcriptome](https://doi.org/10.1101/2025.10.14.682378) | - |
| 2025 | arXiv | HEP-JEPA | [HEP-JEPA: A foundation model for collider physics using joint embedding predictive architecture](https://arxiv.org/abs/2502.03933) | [Project](https://hep-jepa.github.io/) |
| 2025 | arXiv | - | [Joint Embedding Predictive Architecture for self-supervised pretraining on polymer molecular graphs](https://arxiv.org/abs/2506.18194) | - |
| 2025 | bioRxiv | - | [Understanding neural circuit principles for representation learning through joint-embedding predictive architectures](https://doi.org/10.1101/2025.11.25.690220) | - |
| 2024 | NeurIPS Workshop | - | [Learning Symmetry-Independent Jet Representations via Jet-Based Joint Embedding Predictive Architecture](https://arxiv.org/abs/2412.05333) | - |

### Remote Sensing

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | AlignJEPA | [AlignJEPA: Predictive Vision-Language Alignment for Remote Sensing Foundation Models](https://arxiv.org/abs/2608.15456) | - |
| 2026 | arXiv | ChangeJEPA | [ChangeJEPA: Predict Before You Compare for Remote Sensing Change Detection](https://arxiv.org/abs/2611.05570) | [Project](https://buddhi19.github.io/ChangeJEPA) |
| 2026 | arXiv | CR-JEPA | [CR-JEPA: Cross-Modal Joint-Embedding Predictive Learning for Remote Sensing Image Retrieval](https://arxiv.org/abs/2606.00706) | - |
| 2026 | CVPR Workshop | GeoMeld | [GeoMeld: Toward Semantically Grounded Foundation Models for Remote Sensing](https://arxiv.org/abs/2604.10591) | - |
| 2026 | SSRN | - | [Geospatial Anomaly Detection Via Kalman-Inspired Latent-State Estimation V-Jepa V2 As A Learned Process Model For Persistent Satellite Area-Of-Interest Monitoring](https://doi.org/10.2139/ssrn.6521219) | - |
| 2026 | arXiv | JEDI | [JEDI: JEPA-to-Edge Distillation for Efficient Cropland Segmentation from Satellite Imagery](https://arxiv.org/abs/2609.07915) | - |
| 2026 | LNCS | MorphJEPA | [MorphJEPA: Morphology-Aware Latent Prediction for Hyperspectral Images](https://doi.org/10.1007/978-3-032-37595-7_38) | - |
| 2026 | arXiv | RS-JEPA | [RS-JEPA: Remote Sensing Joint-Embedding Predictive Architecture with Scan-Path Views for Cross-Sensor Image Retrieval](https://arxiv.org/abs/2611.14496) | [Code](https://github.com/Tanishq251/RSJEPA) |
| 2026 | ICLR Workshop | Sat-JEPA-Diff | [Sat-JEPA-Diff: Bridging Self-Supervised Learning and Generative Diffusion for Remote Sensing](https://arxiv.org/abs/2603.13943) | [Code](https://github.com/VU-AIML/SAT-JEPA-DIFF) |
| 2026 | Remote Sensing Applications Society and Environment | - | [Sensor-specialized JEPA foundation models complement planetary-scale embeddings for agentic hydrologic reasoning](https://doi.org/10.1016/j.rsase.2026.102136) | - |
| 2026 | arXiv | T-JEPA | [T-JEPA: A Temporal Joint-Embedding Predictive Architecture for Learning Better Remote Sensing Representations](https://arxiv.org/abs/2610.05731) | - |
| 2026 | TGRS | T-SAR-JEPA | [T-SAR-JEPA: Self-Supervised Temporal Anomaly Detection in SAR Amplitude Stacks via Latent Prediction](https://arxiv.org/abs/2606.05700) | [Code](https://github.com/TerraLatent/t-sar-jepa) |
| 2026 | Pattern Recognition Letters | UA-JEPA | [UA-JEPA: Uncertainty-aware joint-embedding predictive learning for remote sensing image retrieval](https://doi.org/10.1016/j.patrec.2026.08.007) | - |
| 2026 | WACV | X-JEPA | [X-JEPA: A Novel Joint Learning Cross-Modal Predictive Alignment Framework for Remote Sensing Image Retrieval](https://doi.org/10.1109/wacv61042.2026.00424) | - |
| 2025 | arXiv | GeoJEPA | [GeoJEPA: Towards Eliminating Augmentation- and Sampling Bias in Multimodal Geospatial Learning](https://arxiv.org/abs/2503.05774) | - |
| 2025 | CVPR Workshop | REJEPA | [REJEPA: A Novel Joint-Embedding Predictive Architecture for Efficient Remote Sensing Image Retrieval](https://arxiv.org/abs/2504.03169) | - |
| 2024 | CVPR | AnySat | [AnySat: One Earth Observation Model for Many Resolutions, Scales, and Modalities](https://arxiv.org/abs/2412.14123) | [Code](https://github.com/gastruc/AnySat) |
| 2023 | Isprs Journal of Photogrammetry and Remote Sensing | - | [Predicting Gradient is Better: Exploring Self-Supervised Learning for SAR ATR with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2311.15153) | [Code](https://github.com/waterdisappear/SAR-JEPA) |

### Audio, Speech and Music

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | Interspeech | ArtNet | [ArtNet: A JEPA-Like Articulatory Predictive Framework for Robust Zero-Shot Phoneme Recognition](https://arxiv.org/abs/2606.16595) | - |
| 2026 | arXiv | S-JEPA | [Cluster Assignments in Soft Targets Shape Speech Representations: Evidence from S-JEPA](https://arxiv.org/abs/2608.19084) | - |
| 2026 | arXiv | CoJEPA | [CoJEPA: Combining Contrastive Learning and JEPA for Global-Local Music Representations](https://arxiv.org/abs/2608.30974) | - |
| 2026 | arXiv | Echo | [Echo: A Joint-Embedding Predictive Architecture for Speaker Diarization and Speech Recognition in a Shared Latent Space](https://arxiv.org/abs/2606.01909) | - |
| 2026 | IEEE Access | Emotion-JEPA | [Emotion-JEPA: Predictive Visual Adaptation and Audio-Modulated Fusion for Multimodal Emotion Recognition](https://doi.org/10.1109/access.2026.3753538) | - |
| 2026 | arXiv | GLaS-JEPA | [GLaS-JEPA: Gaussian-Regularized Speech SSL without Engineered Prediction Targets](https://arxiv.org/abs/2609.37798) | - |
| 2026 | arXiv | MIDI-RAE-JEPA | [MIDI-RAE-JEPA: Hierarchical Representation Learning and Generation for Symbolic Music](https://arxiv.org/abs/2607.14537) | - |
| 2026 | arXiv | Music-JEPA | [Music-JEPA: Learning a World Model of Sound from Action](https://arxiv.org/abs/2607.22000) | - |
| 2026 | arXiv | S-JEPA | [S-JEPA : Soft Clustering Anchors for Self-Supervised Speech Representation Learning](https://arxiv.org/abs/2606.19398) | [Code](https://github.com/gioannides/s-jepa) |
| 2026 | arXiv | - | [Soft Clustering Anchors for Self-Supervised Speech Representation Learning in Joint Embedding Prediction Architectures](https://arxiv.org/abs/2602.09040) | [Code](https://github.com/gioannides/clustering-anchored-jepa) |
| 2026 | arXiv | - | [Synchronized Three-Dimensional Vocal-Tract Motion for Speech Synchronization via Joint-Embedding Predictive Architecture Alignment](https://arxiv.org/abs/2607.11772) | - |
| 2026 | arXiv | Synth-JEPA | [Synth-JEPA: Joint Embedding Prediction for Renderer-Free Synthesizer Parameter Search](https://arxiv.org/abs/2609.31024) | - |
| 2025 | ICME | Audio-JEPA | [Audio-JEPA: Joint-Embedding Predictive Architecture for Audio Representation Learning](https://arxiv.org/abs/2507.02915) | - |
| 2025 | NeurIPS Workshop | - | [JEPA as a Neural Tokenizer: Learning Robust Speech Representations with Density Adaptive Attention](https://arxiv.org/abs/2512.07168) | - |
| 2025 | IEEE Workshop on Applications of Signal Processing to… | - | [Self-Supervised Representation Learning with a JEPA Framework for Multi-instrument Music Transcription](https://doi.org/10.1109/waspaa66052.2025.11230951) | - |
| 2025 | arXiv | WavJEPA | [WavJEPA: Semantic learning unlocks robust audio foundation models for raw waveforms](https://arxiv.org/abs/2509.23238) | - |
| 2025 | ICASSP | - | [Zero-shot Musical Stem Retrieval with Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2411.19806) | - |
| 2024 | ICASSP Workshop | - | [Investigating Design Choices in Joint-Embedding Predictive Architectures for General Audio Representation Learning](https://arxiv.org/abs/2405.08679) | - |
| 2024 | IEEE Open Journal of Signal Processing | JEP-KD | [JEP-KD: Joint-Embedding Predictive Architecture Based Knowledge Distillation for Visual Speech Recognition](https://arxiv.org/abs/2403.18843) | - |
| 2024 | ISMIR | Stem-JEPA | [Stem-JEPA: A Joint-Embedding Predictive Architecture for Musical Stem Compatibility Estimation](https://arxiv.org/abs/2408.02514) | - |
| 2023 | arXiv | A-JEPA | [A-JEPA: Joint-Embedding Predictive Architecture Can Listen](https://arxiv.org/abs/2311.15830) | - |

### Language and Reasoning

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | Applied Sciences | - | [A JEPA-Inspired Span-Masked Framework for Language Representation Learning: Revisiting Cosine Similarity and VICReg Regularization](https://doi.org/10.3390/app16178530) | - |
| 2026 | arXiv | BERT-JEPA | [BERT-JEPA: Reorganizing CLS Embeddings for Language-Invariant Semantics](https://arxiv.org/abs/2601.00366) | - |
| 2026 | arXiv | - | [Beyond Textual Chain-of-Thought: JEPA-Conditioned Latent Reasoning for Large Audio Language Models](https://arxiv.org/abs/2609.34407) | - |
| 2026 | arXiv | ER-JEPA | [ER-JEPA: Experience Replay Improves Joint-Embedding Predictive Learning in Language Models](https://arxiv.org/abs/2609.36952) | - |
| 2026 | arXiv | - | [Predict and Reconstruct: Joint Objectives for Self-Supervised Language Representation Learning](https://arxiv.org/abs/2606.05173) | [Code](https://github.com/aymen-000/predict-reconstruct-language-models) |
| 2026 | EMNLP | - | [Predicting the Next State Is Not Enough: JEPA Representations for Lean Theorem Proving](https://arxiv.org/abs/2609.32908) | - |
| 2026 | arXiv | - | [Prune the Leaky Neurons: Mitigating Private Data Leakage in Fine-Tuned LLMs via Joint-Embedding-Guided Pruning](https://arxiv.org/abs/2610.22792) | - |
| 2026 | arXiv | - | [Representation Without Reward: A JEPA Audit for LLM Fine-Tuning](https://arxiv.org/abs/2605.15394) | - |
| 2026 | SSRN | - | [Semantic Simulation: A Prescriptive Lagrangian Framework for Efficient Semantic Inference — Conservative-by-Construction Language Models and the Shared-Potential Separator, with a Correspondence to Joint Embedding Predictive Architectures](https://doi.org/10.2139/ssrn.6626159) | - |
| 2026 | arXiv | - | [Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA](https://arxiv.org/abs/2602.22617) | [Code](https://github.com/galilai-group/llm-jepa#stp) |
| 2026 | ACM Transactions on Intelligent Systems and Technology | Symbolic-JEPA | [Symbolic-JEPA: Where Symbolic AI Meets Joint-Embedding Predictive Architecture for NL–FOL Conversion](https://doi.org/10.1145/3856815) | - |
| 2026 | arXiv | - | [The JEPA Paradox in Language: The Geometry of Linguistic Alternatives](https://arxiv.org/abs/2607.23531) | - |
| 2025 | arXiv | JEPA-Reasoner | [JEPA-Reasoner: Decoupling Latent Reasoning from Token Generation](https://arxiv.org/abs/2512.19171) | - |
| 2025 | ICLR | LLM-JEPA | [LLM-JEPA: Large Language Models Meet Joint Embedding Predictive Architectures](https://arxiv.org/abs/2509.14252) | [Code](https://github.com/rbalestr-lab/llm-jepa) |
| 2025 | IJCNN Workshop | - | [Speaking in Words, Thinking in Logic: A Dual-Process Framework in QA Systems](https://arxiv.org/abs/2507.20491) | - |
| 2025 | LNCS | Text-JEPA | [Text-JEPA: A Joint Embedding Predictive Architecture for the Conversion of Natural Language into First-Order Logic](https://doi.org/10.1007/978-3-032-09318-9_14) | - |

### Time Series, Tabular and Trajectories

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [A JEPA Recipe for Tabular Foundation Models](https://arxiv.org/abs/2609.25541) | - |
| 2026 | Buildings | ST-JEPA | [Data-Driven Short-Term Forecasting of Indoor Thermal Fields via ST-JEPA for HVAC Feedforward Regulation](https://doi.org/10.3390/buildings16193866) | - |
| 2026 | arXiv | Distributed JEPA | [Distributed JEPA: A Self-Supervised Framework for Energy Forecasting](https://arxiv.org/abs/2609.17029) | - |
| 2026 | arXiv | - | [Does Joint-Embedding Predictive Architecture Pretraining Help Time Series Forecasting?](https://arxiv.org/abs/2609.31680) | - |
| 2026 | SSRN | Fin-JEPA | [Fin-JEPA: Joint-Embedding Predictive Representation Learning for Financial Time Series](https://doi.org/10.2139/ssrn.6855118) | - |
| 2026 | arXiv | - | [From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring](https://arxiv.org/abs/2607.13651) | - |
| 2026 | ICML | - | [Giving Sensors a Voice: Multimodal JEPA for Semantic Time-Series Embeddings](https://arxiv.org/abs/2605.31580) | - |
| 2026 | arXiv | - | [Hierarchical Self-Supervised Representation Learning Framework for Multivariate Time Series Grounded in ECG Analysis](https://arxiv.org/abs/2607.01145) | - |
| 2026 | International Journal of Artificial Intelligence and… | - | [Joint Embedding Predictive ArchitectureA Framework for the Next Generation of Insurance Underwriting](https://doi.org/10.51483/ijaiml.6.12s.2026.1052-1058) | - |
| 2026 | arXiv | - | [Joint-Embedding Predictive Architecture for Sensor-based Activity Recognition](https://arxiv.org/abs/2607.16350) | - |
| 2026 | Preprints.org | - | [Latent Intent Forecasting for Low-Resource: A JEPA Approach to Amharic Conversational Intelligence Using Dialogue Dataset](https://doi.org/10.20944/preprints202606.0409.v1) | - |
| 2026 | KDD | LeNEPA | [LeNEPA: No-Augmentation Next-Latent Prediction for Time-Series Representation Learning](https://arxiv.org/abs/2607.00958) | [Code](https://github.com/langotime/lenepa-milets-2026) |
| 2026 | arXiv | - | [Market-Conditioned JEPA: Learning from Unpredictable Market Shocks](https://arxiv.org/abs/2611.13572) | - |
| 2026 | International Conference on Image, Vision and Computing | Multi-Criteria JEPA | [Multi-Criteria JEPA: An Energy-Based Joint-Embedding Predictive Architecture with Criterion-Level Masking for Sparse Tabular Self-Supervision](https://doi.org/10.1109/icivc70586.2026.11686623) | - |
| 2026 | Automatic Documentation and Mathematical Linguistics | - | [Multitimeframe Drummond Patches and JEPA Pretraining for Short-Term Retail OHLC Series Forecasting](https://doi.org/10.3103/s0005105526700238) | - |
| 2026 | IV | - | [Online Monitoring Framework for Automotive Time Series Data using JEPA Embeddings](https://arxiv.org/abs/2602.09985) | - |
| 2026 | arXiv | Phys-JEPA | [Phys-JEPA: Physics-Informed Latent World Models for Multivariate Time-Series Forecasting](https://arxiv.org/abs/2606.16076) | - |
| 2026 | arXiv | Pythia | [Pythia: Toward Foundation World Models for Multimodal Time Series](https://arxiv.org/abs/2610.05240) | - |
| 2026 | Mediterranean Conference on Embedded Computing | - | [Riemannian Intent Manifolds for Session-Based Search: A Joint Embedding Predictive Architecture for Intent Forecasting](https://doi.org/10.1109/meco70748.2026.11579082) | - |
| 2026 | arXiv | SC-JEPA | [SC-JEPA: Stabilizing Latent Predictive Learning for Time-Series Anomaly Prediction](https://arxiv.org/abs/2602.04643) | - |
| 2026 | arXiv | SPLICE | [SPLICE: Latent Diffusion over JEPA Embeddings for Conformal Time-Series Inpainting](https://arxiv.org/abs/2605.00126) | - |
| 2026 | arXiv | STOCK-JEPA | [STOCK-JEPA: Prior-Anchored Latent Revision Representation Learning in Equity Markets](https://arxiv.org/abs/2610.07006) | - |
| 2026 | IEEE International Conference on Intelligent… | - | [Unsupervised Industrial Anomaly Detection Using I-JEPA Features](https://doi.org/10.1109/ines69513.2026.11661184) | - |
| 2026 | arXiv | W-JEPA | [W-JEPA: Wavelet Joint-Embedding Predictive Architecture for Wearable Activity Recognition](https://arxiv.org/abs/2610.19411) | - |
| 2025 | International Journal of Aviation Aeronautics and… | - | [Generalizing Classification of Pilot Workload: Transfer Learning versus a JEPA-Inspired Transformer Architecture](https://doi.org/10.58940/2374-6793.1971) | - |
| 2025 | arXiv | HiT-JEPA | [HiT-JEPA: A Hierarchical Self-supervised Trajectory Embedding Framework for Similarity Computation](https://arxiv.org/abs/2507.00028) | - |
| 2025 | AAAI | - | [Koopman Invariants as Drivers of Emergent Time-Series Clustering in Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2511.09783) | - |
| 2025 | KDD | TimeCapsule | [TimeCapsule: Solving the Jigsaw Puzzle of Long-Term Time Series Forecasting with Compressed Predictive Representations](https://arxiv.org/abs/2504.12721) | - |
| 2024 | IEEE Transactions on Network and Service Management | - | [A Deep Learning System for Detecting IoT Web Attacks With a Joint Embedded Prediction Architecture (JEPA)](https://doi.org/10.1109/tnsm.2024.3454777) | - |
| 2024 | arXiv | LaT-PFN | [LaT-PFN: A Joint Embedding Predictive Architecture for In-context Time-series Forecasting](https://arxiv.org/abs/2405.10093) | - |
| 2024 | SIGSPATIAL/GIS | T-JEPA | [T-JEPA: A Joint-Embedding Predictive Architecture for Trajectory Similarity Computation](https://arxiv.org/abs/2406.12913) | - |
| 2024 | IoT-J | - | [Time-Series JEPA for Predictive Remote Control under Capacity-Limited Networks](https://arxiv.org/abs/2406.04853) | - |

### Graphs and Recommendation

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | IJCNN | - | [A self-supervised joint embedding predictive approach for bipartite graphs to solve linear programs](https://doi.org/10.1109/ijcnn69854.2026.11729833) | - |
| 2026 | Innovations in Intelligent Systems and Applications… | FEDBIOJEPA-A | [FEDBIOJEPA-A Self-Supervised Federated Knowledge Graph Framework for Computational Drug Repositioning](https://doi.org/10.1109/asyu71790.2026.11772237) | - |
| 2026 | International Artificial Intelligence and Data… | Graph-JEPA | [Graph-JEPA: Self-Supervised Relational Inference on Heterogeneous Biomedical Graphs for Drug Repositioning](https://doi.org/10.1109/idap71869.2026.11728010) | - |
| 2026 | arXiv | HP-JEPA | [HP-JEPA: Hierarchical Partitioning for Multi-Resolution Graph Joint-Embedding Predictive Learning](https://arxiv.org/abs/2608.00491) | - |
| 2026 | LNCS | MC-JEPA-Hybrid | [MC-JEPA-Hybrid: Integrating OWA Operators and Choquet Integral with Joint-Embedding Predictive Architecture for Enhanced Multi-Criteria Recommendations](https://doi.org/10.1007/978-981-92-2885-0_13) | - |
| 2026 | LNCS | MC-JEPA | [MC-JEPA: A Neural Network Framework with Multi-criteria Aggregation for Recommender Systems](https://doi.org/10.1007/978-981-92-5870-3_16) | - |
| 2026 | arXiv | NodeJEPA | [NodeJEPA: Structure-Conditioned Latent Prediction for Node-Level Graph Self-Supervised Learning](https://arxiv.org/abs/2608.04381) | [Code](https://github.com/OliverZ-dot/Node-Jepa) |
| 2026 | arXiv | Phenomenon-Graph JEPA | [Phenomenon-Graph JEPA: Label-Efficient Representation Learning for Contactless Cardiorespiratory Sensing](https://arxiv.org/abs/2609.32928) | - |
| 2026 | arXiv | - | [Scalable and Efficient Joint Spiking Embedding Predictive Architecture for Large-Scale Dynamic Graphs](https://arxiv.org/abs/2607.18412) | - |
| 2026 | arXiv | - | [Self-Supervised Pretraining of Molecular Graph Encoders with LeJEPA](https://arxiv.org/abs/2609.04261) | - |
| 2026 | bioRxiv | SpatialJEPA | [SpatialJEPA: JEPA-inspired graph-context distillation for spatially aware multiomics integration](https://doi.org/10.64898/2026.07.21.739810) | - |
| 2026 | International Conference on Image, Vision and Computing | TagJEPA | [TagJEPA: A Joint-Embedding Predictive Architecture for Energy-Based Tag-Aware Recommendation](https://doi.org/10.1109/icivc70586.2026.11686699) | - |
| 2026 | arXiv | - | [When Graph-JEPA Learns the Wrong Thing: Diagnosing and Repairing Category-Conditional Collapse](https://arxiv.org/abs/2608.20516) | - |
| 2026 | arXiv | World-as-Graph | [World-as-Graph: Relational World Modeling Through Latent Space Graphs](https://arxiv.org/abs/2609.38927) | - |
| 2025 | arXiv | JEPA4Rec | [JEPA4Rec: Learning Effective Language Representations for Sequential Recommendation via Joint Embedding Predictive Architecture](https://arxiv.org/abs/2504.10512) | - |
| 2025 | IEEE Transactions on Smart Grid | RoadPowerFM | [RoadPowerFM: Graphormer-JEPA-Based Foundation Model for Road-Power Coupling Network](https://doi.org/10.1109/tsg.2025.3578842) | - |
| 2023 | TMLR | - | [Graph-level Representation Learning with Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2309.16014) | [Code](https://github.com/geriskenderi/graph-jepa) |

### Wireless, Networks and Security

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [A JEPA-Based Field-Layer World Model for Bridging Channel Prediction and Estimation](https://arxiv.org/abs/2608.10222) | - |
| 2026 | arXiv | - | [Applying JEPA-Style Predictive Learning to JA4-Derived Network Fingerprints](https://arxiv.org/abs/2607.08465) | - |
| 2026 | arXiv | CommJEPA | [CommJEPA: When Predictive Representation Learning Meets Wireless Intelligence](https://arxiv.org/abs/2611.14961) | - |
| 2026 | arXiv | CSI-JEPA | [CSI-JEPA: Towards Foundation Representations for Ubiquitous Wi-Fi Sensing with Minimal Supervision](https://arxiv.org/abs/2605.14171) | - |
| 2026 | arXiv | - | [Hierarchical JEPA Meets Predictive Remote Control in Beyond 5G Networks](https://arxiv.org/abs/2602.07000) | - |
| 2026 | Electronics | - | [Human-Centric Zero Trust Identity Architecture for the Fifth Industrial Revolution: A JEPA-Driven Approach to Adaptive Identity Governance](https://doi.org/10.3390/electronics15091878) | - |
| 2026 | arXiv | - | [JEPA for AI-Native 6G: Predictive Representations and Open Challenges](https://arxiv.org/abs/2607.09798) | - |
| 2026 | arXiv | - | [JEPA-Inspired Latent Field Prediction for Sparse-Pilot MIMO-OFDM Channel Reconstruction](https://arxiv.org/abs/2610.37391) | - |
| 2026 | arXiv | JEPA-kMMVAE | [JEPA-kMMVAE: CSI Prediction for Time-Varying Wireless Channels](https://arxiv.org/abs/2610.13315) | - |
| 2026 | arXiv | JEPA-MSAC | [JEPA-MSAC: A Joint-Embedding Predictive Architecture for Multimodal Sensing-Assisted Communications](https://arxiv.org/abs/2603.29796) | - |
| 2026 | arXiv | LatentWave | [LatentWave: JEPA Pretraining for Wireless Foundation Models](https://arxiv.org/abs/2606.06373) | - |
| 2026 | Preprints.org | Malware-JEPA | [Malware-JEPA: A Joint-Embedding Predictive Architecture on Heterogeneous Behavior Graphs for Malware Family Classification](https://doi.org/10.20944/preprints202606.1501.v1) | - |
| 2026 | arXiv | - | [Masked Latent Prediction of CSI for Indoor Localization in Integrated Sensing and Communication Systems](https://arxiv.org/abs/2609.08509) | - |
| 2026 | VTC | NEMESIS-Shield | [NEMESIS-Shield: Learning Resilient Signal Representations for GNSS Integrity via JEPA](https://doi.org/10.1109/vtc2026-fall68024.2026.11758470) | - |
| 2026 | Research Square | PhishJEPA | [PhishJEPA – a Transferable Phishing Email-Related Representation Learning](https://doi.org/10.21203/rs.3.rs-11120622/v1) | - |
| 2026 | arXiv | WiFi-JEPA | [WiFi-JEPA: Self-supervised Learning for WiFi-CSI 3D Human Pose Estimation](https://arxiv.org/abs/2607.11064) | - |
| 2026 | arXiv | WirelessJEPA | [WirelessJEPA: A Multi-Antenna Foundation Model using Spatio-temporal Wireless Latent Predictions](https://arxiv.org/abs/2601.20190) | - |
| 2025 | PIMRC | - | [From Pixels to CSI: Distilling Latent Dynamics For Efficient Wireless Resource Management](https://arxiv.org/abs/2506.16216) | - |
| 2024 | IEEE Wireless Communications Letters | - | [Learning Latent Wireless Dynamics from Channel State Information](https://arxiv.org/abs/2409.10045) | - |

### Other

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | SAE technical paper series | - | [A Latent Space Framework for Modeling Transient Engine Emissions Using Joint Embedding Predictive Architectures](https://arxiv.org/abs/2601.19822) | - |
| 2026 | arXiv | - | [JEPA as a Transferable Optimizer: Learning and Understanding Black-Box Optimization from Reward-Agnostic Pretraining](https://arxiv.org/abs/2611.23608) | [Code](https://github.com/mdebnath22/jepa-props) |
| 2026 | LNCS | JEPA-Chain | [JEPA-Chain Engineering Framework: From Theory to Production Deployment in Blockchain Optimization](https://doi.org/10.1007/978-981-92-2885-0_15) | - |
| 2026 | LNCS | - | [Self-supervised Academic Trajectory Prediction on StarkNet Layer 2 Blockchain Using Joint Embedding Predictive Architecture](https://doi.org/10.1007/978-981-92-5870-3_27) | - |

## Related Work That Uses, Evaluates or Discusses JEPA

Papers that are not primarily about a JEPA method but build on, benchmark against, or analyze JEPA models.

#### Related: Surveys and Tutorials

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [From World Models to World Action Models: A Concise Tutorial for Robotics](https://arxiv.org/abs/2607.00836) | [Code](https://github.com/clearlab-sustech/WorldModelSurvey) |
| 2026 | arXiv | - | [Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412) | - |
| 2024 | arXiv | - | [Exploring the Interplay Between Video Generation and World Models in Autonomous Driving: A Survey](https://arxiv.org/abs/2411.02914) | - |
| 2023 | arXiv | - | [A Review on Objective-Driven Artificial Intelligence](https://arxiv.org/abs/2308.10135) | - |

#### Related: Theory and Analysis

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [Auto Researching, not hyperparameter tuning: Convergence Analysis of 10,000 Experiments](https://arxiv.org/abs/2603.15916) | - |
| 2026 | arXiv | - | [Dataset-Level Regularization for Joint-Embedding Self-Supervised Learning](https://arxiv.org/abs/2610.20158) | - |
| 2026 | arXiv | - | [Dual-Channel Grounded World Modeling (DCGWM): Structural Prevention of Objective Interference Collapse via Heterogeneous External Grounding with Inward-Only Gradient Flow](https://arxiv.org/abs/2606.18688) | - |
| 2026 | arXiv | - | [Identifiability Without Gaussianity: Symbolic World Models and Near-Infinite Temporal Consistency](https://arxiv.org/abs/2606.12471) | - |
| 2026 | arXiv | - | [Learn from your own latents and not from tokens: A sample-complexity theory](https://arxiv.org/abs/2605.27734) | - |
| 2026 | arXiv | - | [Local Synaptic Rules Can Implement a SIGReg Gradient Without Backpropagation](https://arxiv.org/abs/2607.21622) | [Code](https://github.com/mdda/biological-sigreg) |
| 2026 | arXiv | - | [Motion-guided Contrastive Regularization For Latent World Models](https://arxiv.org/abs/2611.06901) | - |
| 2026 | arXiv | - | [On the Identifiability of Controlled World Models](https://arxiv.org/abs/2607.22430) | - |
| 2026 | arXiv | - | [Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning](https://arxiv.org/abs/2606.13856) | - |
| 2026 | arXiv | QQWorld | [QQWorld: Quantile-Quantile Matching for World Model Regularization](https://arxiv.org/abs/2607.28415) | - |
| 2026 | arXiv | - | [Regularize or Localize: When Training-Time KV-Cache Geometry Pays Under Quantization](https://arxiv.org/abs/2607.17019) | - |
| 2026 | arXiv | SADL | [SADL: On the Demand-Supply Geometry of Representation Collapse](https://arxiv.org/abs/2611.21596) | - |
| 2026 | arXiv | - | [Spectral Ghost in Representation Learning: A Unified View from Component Analysis to Self-Supervised Learning](https://arxiv.org/abs/2601.20154) | - |
| 2026 | arXiv | - | [The Theory of Mind Utility: A Formal Account of Mentalizing](https://arxiv.org/abs/2606.12721) | - |
| 2026 | arXiv | - | [Unbiased Open World Regularization for Fair Self-Supervised Learning](https://arxiv.org/abs/2607.22149) | - |
| 2026 | ICLR Workshop | Weak-SIGReg | [Weak-SIGReg: Covariance Regularization for Stable Deep Learning](https://arxiv.org/abs/2603.05924) | [Code](https://github.com/kreasof-ai/sigreg) |
| 2026 | arXiv | - | [Why Does the Future Branch? Identifiable Closure Tests for Stochastic Physical World Models](https://arxiv.org/abs/2608.00591) | - |
| 2026 | arXiv | - | [Why Self-Supervised Encoders Want to Be Normal](https://arxiv.org/abs/2604.27743) | - |
| 2025 | ICLR | - | [Is the Reversal Curse a Binding Problem? Uncovering Limitations of Transformers from a Basic Generalization Failure](https://arxiv.org/abs/2504.01928) | - |

#### Related: Image and Static Representation Learning

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [Contrast encodes inductive bias: separating slow noise from dynamics in predictive representation learning](https://arxiv.org/abs/2606.07770) | - |
| 2026 | arXiv | - | [Cross-simulator transfer with foundation model summaries: Towards robust SKA-era reionization inference](https://arxiv.org/abs/2608.26354) | - |
| 2026 | arXiv | - | [Deep Networks Favor Simple Data](https://arxiv.org/abs/2604.00394) | - |
| 2026 | arXiv | - | [Discrete energy as an exact label-free training objective for finite-element surrogates](https://arxiv.org/abs/2608.05437) | - |
| 2026 | ACCV | - | [Drift-adaptive Representation Preservation for Domain-Incremental Learning](https://arxiv.org/abs/2611.06093) | - |
| 2026 | arXiv | Face-Trace | [Face-Trace: Open-Set Attribution and Progressive Discovery of Synthetic Face Generators](https://arxiv.org/abs/2607.07545) | - |
| 2026 | arXiv | - | [Generative Representation Learning for Scalable Latent Tokenization](https://arxiv.org/abs/2610.20533) | - |
| 2026 | arXiv | - | [Generative Uncertainty as a Self-supervised Signal for Semantic Similarity Learning](https://arxiv.org/abs/2609.35341) | - |
| 2026 | NeurIPS | - | [Handwritten Text Recognition Lives in the High-Pixel Variance Subspace](https://arxiv.org/abs/2609.35473) | - |
| 2026 | arXiv | - | [Improving Signals, Declining Encoder: A Known-Answer Test of Label-Free Monitoring in Self-Supervised Learning](https://arxiv.org/abs/2610.35766) | [Code](https://github.com/nilotpal09/improving-signals-declining-encoder) |
| 2026 | Neurocomputing | - | [Masked Generative-Contrastive Representation Learning for Cross-Dataset EEG-Based Emotion Recognition](https://arxiv.org/abs/2607.04139) | - |
| 2026 | arXiv | - | [Physics-Aligned Self-Supervised Learning for Scientific Imaging](https://arxiv.org/abs/2607.28868) | - |
| 2026 | arXiv | PredErase | [PredErase: Training-Free Object-and-Effect Removal with Predictive Latent Guidance](https://arxiv.org/abs/2609.00956) | [Code](https://github.com/xiuwk0820-collab/PredErase) |
| 2026 | arXiv | SEEC | [SEEC: A Large-Scale Dataset and Benchmark for Self-Supervised External-Eye Representation Learning](https://arxiv.org/abs/2611.26386) | [Project](https://monkeygobah.github.io/seec-project/) |
| 2026 | arXiv | - | [Self-Distillation of Hidden Layers for Self-Supervised Representation Learning](https://arxiv.org/abs/2603.15553) | - |
| 2026 | arXiv | Self-Soupervision | [Self-Soupervision: Cooking Model Soups without Labels](https://arxiv.org/abs/2602.02890) | [Code](https://github.com/antofuller/self_soupervision) |
| 2026 | NeurIPS Workshop | - | [Speedrunning Relational Foundation Model Pretraining](https://arxiv.org/abs/2610.28855) | [Code](https://github.com/kunumi/nanoRT) |
| 2026 | arXiv | Stylistic-STORM (ST-STORM) | [Stylistic-STORM (ST-STORM) : Perceiving the Semantic Nature of Appearance](https://arxiv.org/abs/2604.16086) | - |
| 2026 | NeurIPS Workshop | - | [The microscope is the mask: privileged views and labels from a cryo-ET forward model](https://arxiv.org/abs/2609.04325) | - |
| 2026 | arXiv | TorchLean | [TorchLean: Formalizing Neural Networks in Lean](https://arxiv.org/abs/2602.22631) | - |
| 2026 | arXiv | ViTAMINS | [ViTAMINS: An Empirical Study of Training Self-Supervised Vision Transformers with Synthetic Hard Negatives](https://arxiv.org/abs/2609.01041) | - |
| 2026 | arXiv | WALDO | [WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes with World-Model Features](https://arxiv.org/abs/2608.28216) | - |
| 2026 | arXiv | - | [Zero-Shot Cross-City Generalization in End-to-End Autonomous Driving: Self-Supervised versus Supervised Representations](https://arxiv.org/abs/2603.11417) | - |
| 2025 | arXiv | PiLaMIM | [PiLaMIM: Toward Richer Visual Representations by Integrating Pixel and Latent Masked Image Modeling](https://arxiv.org/abs/2501.03005) | - |
| 2024 | CoRL | Sparsh | [Sparsh: Self-supervised touch representations for vision-based tactile sensing](https://arxiv.org/abs/2410.24090) | [Project](https://sparsh-ssl.github.io/) |
| 2024 | NeurIPS | - | [You Don't Need Domain-Specific Data Augmentations When Scaling Self-Supervised Learning](https://arxiv.org/abs/2406.09294) | - |

#### Related: Video and Temporal Prediction

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2027 | WACV | HiVE-VQA | [HiVE-VQA: Hierarchical Interaction via Volumetric Embedding for Video Quality Assessment](https://arxiv.org/abs/2611.17146) | [Code](https://github.com/RobHam99/HiVE-VQA) |
| 2026 | arXiv | Action100M | [Action100M: A Large-scale Video Action Dataset](https://arxiv.org/abs/2601.10592) | - |
| 2026 | arXiv | - | [Beyond the Beep: Scalable Collision Anticipation and Real-Time Explainability with BADAS-2.0](https://arxiv.org/abs/2604.05767) | - |
| 2026 | arXiv | - | [Can a World Model Predict a Deepfake Video? A Consistency Margin Prior for Deepfake Detection](https://arxiv.org/abs/2611.21846) | - |
| 2026 | arXiv | - | [Detecting Temporal Concepts in Video Transformers via a No-False-Positives Test](https://arxiv.org/abs/2610.33353) | - |
| 2026 | arXiv | EviBridge | [EviBridge: Encoding Predictive Visual Evidence for Proactive Interaction](https://arxiv.org/abs/2611.20916) | - |
| 2026 | ITSC | FLaRA | [FLaRA: Predicting Future Latent Representations for Accident Anticipation](https://arxiv.org/abs/2606.14380) | - |
| 2026 | arXiv | - | [From Pixels to Newtons: Predicting In Vivo Joint Contact Forces from Monocular Video](https://arxiv.org/abs/2606.06631) | - |
| 2026 | arXiv | FROST-STA | [FROST-STA: Frozen Dense Features for the Ego4D Short-Term Object Interaction Anticipation](https://arxiv.org/abs/2606.00694) | - |
| 2026 | NeurIPS Workshop | - | [How Do Video Foundation Models Encode Intuitive Physics? Probing Across Pretraining Paradigms](https://arxiv.org/abs/2606.09646) | - |
| 2026 | arXiv | - | [Latent-Action-Guided Video-Language Feature Learning for Surgical Instrument-Tissue Interaction Recognition](https://arxiv.org/abs/2607.19889) | - |
| 2026 | arXiv | - | [Learning from Next-Frame Prediction: Towards Unified and Scalable Visual World Modeling](https://arxiv.org/abs/2610.30724) | - |
| 2026 | arXiv | MoRAE | [MoRAE: Flow-Friendly Self-Supervised Latents for Text-to-Motion Generation](https://arxiv.org/abs/2607.29180) | - |
| 2026 | BMVC | - | [Off-Manifold Refinement: Guiding Video Generators with a Frozen World Model](https://arxiv.org/abs/2608.29904) | [Project](https://itruonghai.github.io/omr) |
| 2026 | CVPR Workshop | PlayClass | [PlayClass: Automated Play Behaviour Classification in Poultry](https://arxiv.org/abs/2605.27304) | - |
| 2026 | NeurIPS Workshop | - | [Probing Where Surprise Happens: Localized Violation-of-Expectation Evaluation of Video World Models](https://arxiv.org/abs/2611.18979) | - |
| 2026 | ICLR Workshop | - | [Representation Learning for Spatiotemporal Physical Systems](https://arxiv.org/abs/2603.13227) | [Code](https://github.com/helenqu/physical-representation-learning) |
| 2026 | arXiv | SurgMotion | [SurgMotion: A Video-Native Foundation Model for Universal Understanding of Surgical Videos](https://arxiv.org/abs/2602.05638) | - |
| 2026 | arXiv | - | [The Invisible Hand of Physics: When Video Diffusion Models Know More Than They Show](https://arxiv.org/abs/2606.05328) | - |
| 2026 | arXiv | The TIME Machine | [The TIME Machine: On The Power of Motion for Efficient Perception](https://arxiv.org/abs/2605.23045) | [Project](https://time-model.github.io/) |
| 2026 | arXiv | TrAction | [TrAction: Action Recognition with Sparse Trajectories](https://arxiv.org/abs/2606.03490) | [Code](https://github.com/ecker-lab/TrAction) |
| 2026 | arXiv | TrajPred | [TrajPred: Trajectory-Conditioned Joint Embedding Prediction for Surgical Instrument-Tissue Interaction Recognition in Vision-Language Models](https://arxiv.org/abs/2603.06999) | - |
| 2026 | NeurIPS | TT-VidT | [TT-VidT: Decoupling the Temporal Axis for Efficient Motion-Centric Video Pretraining](https://arxiv.org/abs/2609.33419) | [Project](https://kohakublueleaf.github.io/TTVidT/) |
| 2026 | arXiv | VidaForge | [VidaForge: Open Research Infrastructure for Video Pretraining Data Recipes](https://arxiv.org/abs/2609.06652) | [Code](https://github.com/GAIR-NLP/VidaForge) |
| 2026 | ECCV | - | [Video Generation Models are General-Purpose Vision Learners](https://arxiv.org/abs/2607.09024) | [Project](https://genception.github.io) |
| 2026 | arXiv | - | [What, Where, and How: Probing Spatiotemporal Representations in Video Foundation Models](https://arxiv.org/abs/2609.01551) | - |
| 2026 | NeurIPS Workshop | - | [When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?](https://arxiv.org/abs/2611.01815) | - |
| 2026 | arXiv | - | [Zero-Shot Object Re-Identification in Egocentric Kitchen Videos via Multi-Stage SAM3 Feature Fusion](https://arxiv.org/abs/2605.26383) | - |
| 2025 | arXiv | BADAS | [BADAS: Context Aware Collision Prediction Using Real-World Dashcam Data](https://arxiv.org/abs/2510.14876) | - |
| 2025 | NeurIPS | DisMo | [DisMo: Disentangled Motion Representations for Open-World Motion Transfer](https://arxiv.org/abs/2511.23428) | [Project](https://compvis.github.io/DisMo) |
| 2025 | CVPR Workshop | - | [Domain-Adaptive Pretraining Improves Primate Behavior Recognition](https://arxiv.org/abs/2509.12193) | [Code](https://github.com/ecker-lab/dap-behavior) |
| 2025 | arXiv | - | [Inferring Dynamic Physical Properties from Video Foundation Models](https://arxiv.org/abs/2510.02311) | [Project](https://www.robots.ox.ac.uk/~vgg/research/idpp/) |
| 2025 | CVPR | PriVi | [PriVi: Towards A General-Purpose Video Model For Primate Behavior In The Wild](https://arxiv.org/abs/2511.09675) | - |
| 2025 | CVPR | - | [Recurrent Video Masked Autoencoders](https://arxiv.org/abs/2512.13684) | - |
| 2024 | TMLR | V-JEPA | [Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471) | - |

#### Related: Action-Conditioned World Models, Planning and Control

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | $Σ$-LeWM | [$Σ$-LeWM: Learning World Models via S-Information for Robot Control](https://arxiv.org/abs/2611.12732) | - |
| 2026 | arXiv | 4LC | [4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling](https://arxiv.org/abs/2610.17625) | [Project](https://zgca-hmi-lab.github.io/4LC) |
| 2026 | arXiv | - | [Abductive World Modeling via Causal Representation Learning](https://arxiv.org/abs/2609.36985) | - |
| 2026 | arXiv | AD-WM | [AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control](https://arxiv.org/abs/2609.30264) | [Project](https://ad-wm.github.io/) |
| 2026 | CoRL Workshop | - | [Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation](https://arxiv.org/abs/2610.35636) | - |
| 2026 | arXiv | - | [Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think](https://arxiv.org/abs/2609.30036) | - |
| 2026 | arXiv | ALPS | [ALPS: Visual State Encoders for World Models](https://arxiv.org/abs/2610.30120) | [Code](https://github.com/UCSC-VLAA/ALPS) |
| 2026 | Journal of Advanced Robotics, Autonomous Systems and… | ARYA | [ARYA: A Physics-Constrained Composable & Deterministic World Model Architecture](https://arxiv.org/abs/2603.21340) | - |
| 2026 | arXiv | ATLAS | [ATLAS: Aligned Transport of Latent Structure for Reliable World Model Planning](https://arxiv.org/abs/2609.36333) | - |
| 2026 | arXiv | - | [Beyond a single latent space: a dual-latent world model for long-horizon planning](https://arxiv.org/abs/2609.37644) | [Code](https://github.com/DeLin1001/Dual-WM-Official) |
| 2026 | arXiv | - | [Beyond One-Step Accuracy: State-Affine Latent Transition for Reliable Visual Planning](https://arxiv.org/abs/2609.33595) | - |
| 2026 | arXiv | - | [Beyond the Next Step: Variable-Length Latent World Models for Long-Horizon Planning](https://arxiv.org/abs/2606.21775) | - |
| 2026 | arXiv | - | [Certified World Models as Sensing Clocks: Drift-Aware Deadlines for Active Perception](https://arxiv.org/abs/2607.01537) | - |
| 2026 | arXiv | - | [Control-Geometry Straightening for Sampling-Based Latent Planning](https://arxiv.org/abs/2609.35603) | - |
| 2026 | arXiv | Copper-Policy | [Copper-Policy: Focus on the Representation for Robust Robot Manipulation](https://arxiv.org/abs/2609.32779) | [Project](https://zexinfeng-cn.github.io/works/copper-policy/) |
| 2026 | arXiv | - | [Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned Objectives for MPC Planning](https://arxiv.org/abs/2608.18746) | - |
| 2026 | arXiv | Devol-ONE | [Devol-ONE: One Autoregressive Mixture of Transformers to Unify Vision-Language-Action and Latent World Modeling](https://arxiv.org/abs/2609.32193) | - |
| 2026 | arXiv | - | [Diffusion Transformer World-Action Model for AV Scene Prediction](https://arxiv.org/abs/2606.12987) | - |
| 2026 | arXiv | - | [Directed Temporal Representations for Offline Visual Control](https://arxiv.org/abs/2610.08960) | - |
| 2026 | arXiv | - | [Dissipative Learning: A Framework for Viable Adaptive Systems](https://arxiv.org/abs/2601.17933) | - |
| 2026 | arXiv | DOCK | [DOCK: Dual-Stream-Inspired Self-Supervised Object-Centric Representations Grounded in Robot Kinematics](https://arxiv.org/abs/2611.23578) | - |
| 2026 | arXiv | Dreamer-CDP | [Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction](https://arxiv.org/abs/2603.07083) | - |
| 2026 | arXiv | DreamX-Phi 1.0 | [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489) | [Code](https://github.com/AMAP-ML/DreamX-Phi) |
| 2026 | arXiv | DroneWAM | [DroneWAM: Efficient World Action Model for Drone Visual Navigation](https://arxiv.org/abs/2609.33148) | [Code](https://github.com/1e12Leon/DroneWAM) |
| 2026 | arXiv | - | [DSGE as a Structured World Model:Benchmarking Counterfactual Generalization in Economic Worlds](https://arxiv.org/abs/2607.03144) | - |
| 2026 | arXiv | DUET-DINO | [DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation](https://arxiv.org/abs/2609.10506) | [Project](https://utn-air.github.io/DUET-DINO) |
| 2026 | arXiv | DynaWM | [DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation](https://arxiv.org/abs/2607.02604) | - |
| 2026 | arXiv | - | [Escaping Latent Traps by Remembering: Training-Free Episodic Kernel Repulsion for World-Model Planning](https://arxiv.org/abs/2611.22470) | - |
| 2026 | arXiv | EVEWorld | [EVEWorld: Physical Evolution Supervision for Embodied World Models](https://arxiv.org/abs/2610.03374) | - |
| 2026 | arXiv | FARM | [FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model](https://arxiv.org/abs/2609.11445) | - |
| 2026 | arXiv | Fast-LeWM | [Fast LeWorldModel](https://arxiv.org/abs/2606.26217) | - |
| 2026 | arXiv | FIRM-WM | [FIRM-WM: State-factorized factual-interventional recurrent modeling for reward-free visual planning](https://arxiv.org/abs/2609.22816) | - |
| 2026 | arXiv | ForeDrive | [ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](https://arxiv.org/abs/2609.26299) | - |
| 2026 | arXiv | - | [From Generation to Simulation: How Far Are World Models from Being True Simulators?](https://arxiv.org/abs/2608.23070) | [Code](https://github.com/AtongWang/world-model-simulators) |
| 2026 | arXiv | GLAM | [GLAM: Training a latent world model over global spatiotemporal memory for active exploration and navigation](https://arxiv.org/abs/2609.14561) | - |
| 2026 | arXiv | - | [Grounded World Model: Latent Planning with Language Goals](https://arxiv.org/abs/2604.11751) | [Project](https://quanyili.github.io/gwm-wiser/) |
| 2026 | arXiv | - | [Helping Music Co-Creation Agents 'Listen' Well: Hierarchical Self-Supervised World Models for Understanding and Generation](https://arxiv.org/abs/2608.04378) | [Project](https://drscotthawley.github.io/midi-rae-jepa-son/) |
| 2026 | arXiv | - | [How Long, Not How Close: A Learned Temporal Metric for Planning in Latent World Models](https://arxiv.org/abs/2610.04988) | - |
| 2026 | Proc. Mach. Learn. Res. 306: | - | [Improving Diffusion Planners by Self-Supervised Action Gating with Energies](https://arxiv.org/abs/2603.02650) | - |
| 2026 | CVPR | - | [Inference-time Physics Alignment of Video Generative Models with Latent World Models](https://arxiv.org/abs/2601.10553) | - |
| 2026 | arXiv | - | [Infrastructure-Centric World Models: Bridging Temporal Depth and Spatial Breadth for Roadside Perception](https://arxiv.org/abs/2604.17651) | - |
| 2026 | arXiv | JointGV | [JointGV: Structure-Aware Correction of Visual World Models with Parallel Graph Dynamics for Long-Horizon Modeling](https://arxiv.org/abs/2611.22543) | - |
| 2026 | arXiv | Kepler-Encoder-v0.1 | [Kepler-Encoder-v0.1: Towards a Multimodal Embedding Model for Robots](https://arxiv.org/abs/2607.13522) | - |
| 2026 | arXiv | LaLa-World | [LaLa-World: Scaling Latent World Models with Natural Language Actions](https://arxiv.org/abs/2610.27851) | [Code](https://github.com/junha1125/LaLa-World) |
| 2026 | arXiv | - | [Latent Energy Action Planning with World Models](https://arxiv.org/abs/2609.03294) | - |
| 2026 | arXiv | - | [Latent Geometry Beyond Search: Amortizing Planning in World Models](https://arxiv.org/abs/2605.08732) | [Code](https://github.com/hdnndh/Latent-Geometry-Beyond-Search-Amortizing-Planning-in-World-Models) |
| 2026 | arXiv | - | [Latent Goal Prediction from Language for Model-Based Planning](https://arxiv.org/abs/2606.20627) | - |
| 2026 | CoRL Workshop | - | [Latent Projection for Latent Planning](https://arxiv.org/abs/2610.26979) | [Code](https://github.com/yjang43/lp2) |
| 2026 | arXiv | - | [Latent Telepathy: Multi-Robot Communication with Self-Supervised Perceptual Latents](https://arxiv.org/abs/2609.23269) | - |
| 2026 | arXiv | - | [Latent World Models Should Plan with Distances Along the Latent Manifold](https://arxiv.org/abs/2610.25013) | - |
| 2026 | arXiv | - | [Learning Commute-Time-Preserving World Models for Planning](https://arxiv.org/abs/2610.01373) | - |
| 2026 | arXiv | - | [Learning Goal-Conditioned Subgoals through Frozen Hierarchical World Models](https://arxiv.org/abs/2610.26179) | - |
| 2026 | arXiv | - | [Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum](https://arxiv.org/abs/2611.17529) | - |
| 2026 | arXiv | LeCompass | [LeCompass: Task-Level Execution through State-Indexed Interfaces](https://arxiv.org/abs/2611.25679) | - |
| 2026 | arXiv | LeCuration | [LeCuration: A Tiny World Model as a Data Curation Multi-Tool](https://arxiv.org/abs/2610.09285) | - |
| 2026 | arXiv | LePlanner | [LePlanner: An Iterative Amortized Controller For World Models](https://arxiv.org/abs/2609.13845) | - |
| 2026 | arXiv | - | [Library of Hands: Fix the Hands, Not the World Model](https://arxiv.org/abs/2611.12678) | - |
| 2026 | arXiv | Metro-WM | [Metro-WM: Long-Horizon Latent Planning with Realisable Sub-Goals](https://arxiv.org/abs/2609.31868) | - |
| 2026 | arXiv | - | [Mind the Gap: Promises and Pitfalls of Hierarchical Planning in LeWorldModel](https://arxiv.org/abs/2607.12547) | - |
| 2026 | arXiv | - | [One Lens, Many Worlds : A Capability-Typed Interface for World-Model Interpretability](https://arxiv.org/abs/2606.09936) | - |
| 2026 | arXiv | - | [One Verdict Is Not Enough: Regression Testing Learned World Models and Their Test Harnesses](https://arxiv.org/abs/2610.41130) | - |
| 2026 | arXiv | - | [One-Step Next-Latent Prediction Is Not a World Model](https://arxiv.org/abs/2609.36227) | - |
| 2026 | arXiv | OnlyAct | [OnlyAct: Extracting Action Representations from Foundation Models for World Models](https://arxiv.org/abs/2611.14420) | - |
| 2026 | arXiv | - | [Parallel Predictive World Models for Accurate and Efficient Long-Horizon Planning](https://arxiv.org/abs/2610.08627) | - |
| 2026 | arXiv | PAVE | [PAVE: Predictive Alignment and Value-Guided Evolution for World-Action Policies](https://arxiv.org/abs/2608.30378) | - |
| 2026 | arXiv | - | [Predictive but Not Plannable: RC-aux for Latent World Models](https://arxiv.org/abs/2605.07278) | [Code](https://github.com/Guang000/RC-aux) |
| 2026 | arXiv | - | [Predictive Training with Latent Imagination for Visual Quadruped Navigation](https://arxiv.org/abs/2607.17574) | - |
| 2026 | arXiv | ProWorld | [ProWorld: Progress-Aware Hyperbolic World Models for Long-Horizon Visual Goal Reaching](https://arxiv.org/abs/2608.01926) | - |
| 2026 | arXiv | - | [Readout and Operating-Point Sensitivity in Event-Stream Candidate Selection](https://arxiv.org/abs/2610.36743) | - |
| 2026 | arXiv | - | [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](https://arxiv.org/abs/2605.06388) | - |
| 2026 | arXiv | RESETTLE | [RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control](https://arxiv.org/abs/2610.12185) | [Code](https://github.com/JIA-Lab-research/RESETTLE) |
| 2026 | arXiv | - | [Rethinking Actions: Continuity-Aware Priors for World-Model Planning](https://arxiv.org/abs/2611.16645) | - |
| 2026 | arXiv | SAGE | [SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning](https://arxiv.org/abs/2607.17973) | - |
| 2026 | arXiv | - | [Search or Scoring? Diagnosing Why Visual World-Model Planners Fail](https://arxiv.org/abs/2611.25347) | - |
| 2026 | arXiv | - | [See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space](https://arxiv.org/abs/2610.31762) | [Project](https://wang-yinxi.github.io/representnav/) |
| 2026 | arXiv | - | [Semantic Role-Structured World Model for Physical Interaction Planning](https://arxiv.org/abs/2608.22294) | - |
| 2026 | arXiv | - | [Sensorimotor World Models: Perception for Action via Inverse Dynamics](https://arxiv.org/abs/2606.20104) | - |
| 2026 | arXiv | - | [Spoofing the Latent State: Imperceptible Goal-Image Attacks Derail Planning in LeWorldModel](https://arxiv.org/abs/2611.00427) | - |
| 2026 | arXiv | - | [Temporal Straightening for Latent Planning](https://arxiv.org/abs/2603.12231) | - |
| 2026 | arXiv | - | [Temporally Centered SIGReg Improves LeWorldModel Representations for Robot Policy Learning](https://arxiv.org/abs/2607.26924) | - |
| 2026 | arXiv | TERRA | [TERRA: Task-Embedded Reasoning and Representation Architecture for Cross-Domain Applications](https://arxiv.org/abs/2606.01520) | - |
| 2026 | arXiv | - | [Testing World Models on Actions They Have Never Seen: Held-Out Plans, Forecast Accuracy and Price Rules in Retail](https://arxiv.org/abs/2611.22537) | - |
| 2026 | arXiv | - | [The Evaluation Protocol Determines the Result: An Independent Reproduction of LeWorldModel on TwoRoom](https://arxiv.org/abs/2608.10145) | [Code](https://github.com/joyjeet-singh/tinylab) |
| 2026 | arXiv | - | [The Global Neural World Model: Spatially Grounded Discrete Topologies for Action-Conditioned Planning](https://arxiv.org/abs/2604.16585) | - |
| 2026 | arXiv | - | [The Intervention Gap in Latent World Models](https://arxiv.org/abs/2608.29998) | - |
| 2026 | arXiv | - | [The Missing Knowledge Layer in Cognitive Architectures for AI Agents](https://arxiv.org/abs/2604.11364) | - |
| 2026 | arXiv | - | [The Objective Is the Bottleneck: Latent World Models Encode What Their Planners Cannot Use](https://arxiv.org/abs/2608.12959) | - |
| 2026 | arXiv | - | [The Sense Paradigm for World Models](https://arxiv.org/abs/2611.19796) | - |
| 2026 | arXiv | - | [Toward Active Object Detection for UAVs in the Wild: A Large-Scale Dataset, Benchmark and Method](https://arxiv.org/abs/2607.09078) | [Code](https://github.com/Leo000ooo/LUDO_dataset) |
| 2026 | arXiv | - | [Towards Financial World Modeling](https://arxiv.org/abs/2610.09048) | - |
| 2026 | arXiv | Towards VLA-Dreamer | [Towards VLA-Dreamer: Refining VLA Behavior Using World Models](https://arxiv.org/abs/2609.31313) | - |
| 2026 | arXiv | - | [Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object](https://arxiv.org/abs/2610.07355) | - |
| 2026 | arXiv | Traj-LeWM | [Traj-LeWM: Path-Aware World-Model Planning via Latent Trajectory Cost](https://arxiv.org/abs/2608.14125) | - |
| 2026 | arXiv | TS-WAM | [TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control](https://arxiv.org/abs/2610.21922) | - |
| 2026 | arXiv | - | [Ultrasound Operator Guidance Using World Modeling and Retrieval Based Action Planning](https://arxiv.org/abs/2610.06008) | - |
| 2026 | arXiv | VeriVLA | [VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models](https://arxiv.org/abs/2610.21985) | - |
| 2026 | arXiv | VIScore | [VIScore: Diagnosing Planning-Relevant Quality in Latent World Models](https://arxiv.org/abs/2608.11174) | - |
| 2026 | arXiv | - | [Visual Representation and History Modeling for Navigation World Models](https://arxiv.org/abs/2609.29555) | - |
| 2026 | arXiv | VLA-ULAP | [VLA-ULAP: Interleaving Cloud VLA Calls with Ultra-Lightweight Local Action Prediction at the Edge](https://arxiv.org/abs/2609.18663) | - |
| 2026 | arXiv | VLANeXt Family | [VLANeXt Family: A Systematic Study of VLA Models from Core Recipes to Emerging Paradigms](https://arxiv.org/abs/2602.18532) | [Project](https://dravenalg.github.io/projects/VLANeXt/) |
| 2026 | arXiv | VPFlow | [VPFlow: Value-Predictive Planning with Imperfect World Models for Offline Goal Reaching](https://arxiv.org/abs/2610.27280) | - |
| 2026 | CoRL | - | [What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction](https://arxiv.org/abs/2606.07687) | [Code](https://github.com/k1seul/corl2026-action-relevant-latents) |
| 2026 | arXiv | - | [What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning](https://arxiv.org/abs/2610.21915) | - |
| 2026 | arXiv | - | [When Low Prediction Error Misleads Planning: Diagnosing Representation, Dynamics, and Decision Failures in Latent World Models](https://arxiv.org/abs/2610.05550) | - |
| 2026 | arXiv | - | [When to Refine: Selective Search for Frozen Visual World Models](https://arxiv.org/abs/2611.24470) | - |
| 2026 | arXiv | WONDER | [WONDER: A Radio World Model-based Negotiation Framework for Multi-Agent UAV Coverage Optimization](https://arxiv.org/abs/2608.16955) | - |
| 2026 | arXiv | - | [World Model Control by Trajectory Reachability Metrics](https://arxiv.org/abs/2605.22164) | - |
| 2026 | arXiv | world2vec | [world2vec: Mechanistic world models through latent dynamics learning](https://arxiv.org/abs/2610.40637) | - |
| 2026 | arXiv | - | [Write-Protected Discrete Bottlenecks for Language-Grounded World Models: A Structural Limitation and Sufficient Fix](https://arxiv.org/abs/2607.08312) | - |
| 2025 | arXiv | Beyond Generative AI | [Beyond Generative AI: World Models for Clinical Prediction, Counterfactuals, and Planning](https://arxiv.org/abs/2511.16333) | - |
| 2025 | RA-L | Cosmos-Surg-dVRK | [Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning](https://arxiv.org/abs/2510.16240) | - |
| 2025 | arXiv | - | [Large Emotional World Model](https://arxiv.org/abs/2512.24149) | - |
| 2025 | Swiss Conference on Data Science | - | [Learning Actionable World Models for Industrial Process Control](https://arxiv.org/abs/2503.01411) | - |
| 2025 | NeurIPS | - | [Learning from Reward-Free Offline Data: A Case for Planning with Latent Dynamics Models](https://arxiv.org/abs/2502.14819) | [Project](https://latent-planning.github.io/) |
| 2025 | arXiv | MIND-V | [MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment](https://arxiv.org/abs/2512.06628) | - |
| 2025 | ICLR | - | [Stochastic Optimal Control for Continuous-Time fMRI Representation Learning](https://arxiv.org/abs/2502.04892) | - |
| 2024 | arXiv | - | [Learning and Leveraging World Models in Visual Representation Learning](https://arxiv.org/abs/2403.00504) | - |

#### Related: Multimodal

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [A Hierarchical Energy-Based Model for Multimodal Cognition](https://arxiv.org/abs/2608.12398) | - |
| 2026 | arXiv | DART | [DART: A Vision-Language Foundation Model for Comprehensive Rope Condition Monitoring](https://arxiv.org/abs/2605.04943) | - |
| 2026 | arXiv | M* | [M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/abs/2606.12688) | [Code](https://github.com/mstar-project/mstar) |
| 2026 | Proceedings of the 28th International Conference On… | - | [Multimodal Rapport Estimation in Real-World HRI](https://arxiv.org/abs/2608.18401) | - |
| 2026 | arXiv | - | [Non-Contrastive Vision-Language Learning with Predictive Embedding Alignment](https://arxiv.org/abs/2602.00653) | - |
| 2026 | arXiv | PVI | [PVI: Plug-in Visual Injection for Vision-Language-Action Models](https://arxiv.org/abs/2603.12772) | - |
| 2026 | ECCV Workshop | SCOUT | [SCOUT: Sim-to-Real Text-Based Person Retrieval by Embedding-Space Prediction over Frozen Video Features](https://arxiv.org/abs/2609.19483) | [Code](https://github.com/abtraore/SCOUT-ECCV) |
| 2026 | arXiv | - | [Surprise as a Signal for Plasticity and Metacognition](https://arxiv.org/abs/2606.31495) | - |

#### Related: 3D, Structured and Object-Centric

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2027 | Information Sciences 766 | - | [Neural Classifiers as Error-Correcting Codes](https://arxiv.org/abs/2611.18239) | - |
| 2026 | arXiv | - | [Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric World Models](https://arxiv.org/abs/2608.12078) | - |
| 2026 | arXiv | - | [Beyond Geometric Closure: Measuring and Diagnosing Mechanical Consistency in Visual Dynamics](https://arxiv.org/abs/2610.24619) | [Code](https://github.com/BIGPAO123321/mechanical-consistency-visual-dynamics) |
| 2026 | ECCV | DeWorldSG | [DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors](https://arxiv.org/abs/2607.00889) | - |
| 2026 | NeurIPS Workshop | - | [Does LeWorldModel Preserve Local Action Geometry?](https://arxiv.org/abs/2610.31716) | - |
| 2026 | arXiv | Genie 4D | [Genie 4D: Semantic-Prior-Guided 4D Dynamic Scene Reconstruction](https://arxiv.org/abs/2604.09877) | - |
| 2026 | arXiv | Ground-Wing | [Ground-Wing: A Parametric 3D Wing-in-Ground-Effect Dataset for Benchmarking Neural Surrogate Models](https://arxiv.org/abs/2611.04571) | [Code](https://huggingface.co/datasets/andreacenzato/Ground-Wing) |
| 2026 | arXiv | - | [Iterative Erasure Count Is Not an Affine-Invariant Concept Dimension](https://arxiv.org/abs/2608.10566) | - |
| 2026 | arXiv | Polis | [Polis: 3D Self-Supervision at City Scale](https://arxiv.org/abs/2608.29426) | - |
| 2026 | arXiv | - | [Preserve, Then Resolve: Many-to-Many Association and Robust Estimation with General-Purpose Visual Features](https://arxiv.org/abs/2604.23670) | [Code](https://github.com/LIAS-CUHKSZ/preserve_then_resolve) |
| 2026 | arXiv | - | [Revisiting Auxiliary Losses for Conditional Depth Routing: An Empirical Study](https://arxiv.org/abs/2604.17228) | - |
| 2025 | ICML | Locate 3D | [Locate 3D: Real-World Object Localization via Self-Supervised Learning in 3D](https://arxiv.org/abs/2504.14151) | - |

#### Related: Autonomous Driving

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | Latent-WAM++ | [Latent-WAM++: Shaping World and Action Representations for End-to-End Autonomous Driving](https://arxiv.org/abs/2611.10632) | - |
| 2026 | arXiv | SparseWAM | [SparseWAM: Driving World-Action Models are Worth 16 Register Tokens](https://arxiv.org/abs/2611.00044) | - |
| 2026 | arXiv | TriDrive | [TriDrive: Joint Driver, Vehicle, and Road Modeling for Forecasting and Driver Monitoring](https://arxiv.org/abs/2609.33000) | [Code](https://huggingface.co/HenryYHW/TriDrive) |
| 2026 | arXiv | Vault | [Vault: One-Step Latent Generation with Positive-Anchored Rewards for Autonomous Driving](https://arxiv.org/abs/2606.06219) | - |
| 2026 | arXiv | VISTA | [VISTA: A Framework for Vision-Informed Semantic Traffic Awareness](https://arxiv.org/abs/2611.20458) | - |
| 2026 | arXiv | WALT | [WALT: Learning World-Model-Aligned Latent Trajectories for Autonomous Driving](https://arxiv.org/abs/2609.30436) | - |
| 2026 | arXiv | - | [What Do Latent Predictive Vehicle Representations Retain? Measuring State, Geometry, and Local Response](https://arxiv.org/abs/2609.32512) | - |

#### Related: Medical and Healthcare

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [A global predicted-fMRI drive signal from TRIBE does not predict YouTube replay heatmaps](https://arxiv.org/abs/2607.01400) | [Code](https://github.com/mercurialsolo/tribe-replay-heatmaps) |
| 2026 | MICCAI | - | [Benchmarking Video Foundation Models for Remote Parkinson's Disease Screening](https://arxiv.org/abs/2602.13507) | - |
| 2026 | MICCAI | - | [Beyond In-Distribution Metrics: A Systematic Out-of-Distribution Evaluation of Congenital Heart Disease Segmentation](https://arxiv.org/abs/2609.17068) | - |
| 2026 | arXiv | ChronoMedicalWorld | [ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data](https://arxiv.org/abs/2605.21963) | - |
| 2026 | arXiv | CoFlu-Brain | [CoFlu-Brain: An fMRI Connectivity Foundation Model with Cofluctuation-Based Pretraining](https://arxiv.org/abs/2610.15450) | - |
| 2026 | arXiv | - | [Controlled Evaluation of EEG Foundation Models: Random Initialisation, Band-Power and Validation-Selected Probes](https://arxiv.org/abs/2610.32067) | - |
| 2026 | arXiv | - | [Data-Efficient Surgical Phase Segmentation in Small-Incision Cataract Surgery: A Controlled Study of Vision Foundation Models](https://arxiv.org/abs/2604.10514) | [Project](https://sl2005.github.io/DataEfficient-sics-phase-seg/) |
| 2026 | arXiv | - | [Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter Estimation](https://arxiv.org/abs/2607.15492) | - |
| 2026 | MICCAI Workshop | - | [Evaluating the Generalization of Neuroimaging Foundation Models on African Brain MRI](https://arxiv.org/abs/2609.23983) | - |
| 2026 | arXiv | - | [Feature Visualization Recovers Known Cortical Selectivity from TRIBE v2](https://arxiv.org/abs/2605.13904) | [Code](https://github.com/recozers/Tribe-V2-Interp) |
| 2026 | arXiv | FOUND-AF | [FOUND-AF: Benchmarking ECG Foundation Models for Atrial Fibrillation Detection](https://arxiv.org/abs/2608.03597) | - |
| 2026 | arXiv | GLINT | [GLINT: Sparsely Gated Vision-Language Alignment for Fine-Grained Radiology Representations](https://arxiv.org/abs/2606.03180) | [Code](https://github.com/deepnoid-ai/GLINT) |
| 2026 | arXiv | - | [How Much MRI Preprocessing Is Enough? A Cost-Utility Study for Brain MRI Foundation Models](https://arxiv.org/abs/2606.08164) | [Code](https://github.com/PangJiangShuan/PreBrain) |
| 2026 | arXiv | - | [Intervention anchors and scientific verification in synthetic vascular predictive representations](https://arxiv.org/abs/2610.11704) | - |
| 2026 | arXiv | - | [Intervention Granularity Matters: Coherent Treatment Bundles in Counterfactual Simulation with Clinical World Models](https://arxiv.org/abs/2609.21906) | - |
| 2026 | arXiv | LocalProp | [LocalProp: Neuro-Localized Memory-Efficient Backpropagation](https://arxiv.org/abs/2609.32517) | - |
| 2026 | arXiv | LuMamba | [LuMamba: Latent Unified Mamba for Electrode Topology-Invariant and Efficient EEG Modeling](https://arxiv.org/abs/2603.19100) | [Code](https://github.com/pulp-bio/biofoundation) |
| 2026 | arXiv | MorphologyFM | [MorphologyFM: A Foundation Model for Morphology-Aware Representation Learning from ECG and Pulse Oximetry Waveforms](https://arxiv.org/abs/2607.09749) | - |
| 2026 | arXiv | - | [Predicted Cortex Is Not a Domain-General Prior: A Matched-Control Audit of Brain-Encoding Features for Video Memorability](https://arxiv.org/abs/2607.16292) | - |
| 2026 | arXiv | - | [Pretext Matters: An Empirical Study of SSL Methods in Medical Imaging](https://arxiv.org/abs/2603.22649) | - |
| 2026 | arXiv | - | [Pretraining Strategies and Scaling for ECG Foundation Models: A Systematic Study](https://arxiv.org/abs/2605.12241) | - |
| 2026 | NeurIPS Workshop | - | [Repeated-Measure Leakage, Distribution Shift, and Reliability under Partial Observation in Patient World Models](https://arxiv.org/abs/2610.04778) | - |
| 2026 | arXiv | SLICES | [SLICES: A Benchmark and Evaluation Framework for Self-Supervised Learning on Sparse ICU Time Series](https://arxiv.org/abs/2611.18868) | [Code](https://github.com/hannesill/SLICES/tree/ml4h-2026) |
| 2026 | arXiv | - | [Toward Cross-Rubric Surgical Skill Assessment via Joint Embedding Prediction](https://arxiv.org/abs/2611.15125) | - |
| 2026 | ECCV Workshop | - | [Towards Context-Aware Clinical Motion Understanding in Daily Living at Home: Freezing of Gait Detection with Egocentric Vision](https://arxiv.org/abs/2608.13283) | - |
| 2026 | npj Digital Medicine | - | [Video Based Assessment of Surgical Skills Using Frozen Pretrained Video Foundation Models](https://arxiv.org/abs/2609.19772) | - |
| 2026 | arXiv | - | [Your Vision Foundation Model Is Secretly an EEG Foundation Model](https://arxiv.org/abs/2611.17031) | - |
| 2025 | arXiv | - | [Cross-Architecture Knowledge Distillation (KD) for Retinal Fundus Image Anomaly Detection on NVIDIA Jetson Nano](https://arxiv.org/abs/2506.18220) | - |
| 2025 | arXiv | - | [Health system learning achieves generalist neuroimaging models](https://arxiv.org/abs/2511.18640) | - |
| 2025 | arXiv | - | [Integrating Dynamical Systems Learning with Foundational Models: A Meta-Evolutionary AI Framework for Clinical Trials](https://arxiv.org/abs/2506.14782) | - |
| 2025 | arXiv | - | [Predicting Brain Responses To Natural Movies With Multimodal LLMs](https://arxiv.org/abs/2507.19956) | [Code](https://github.com/MedARC-AI/algonauts2025) |
| 2025 | arXiv | SLIM-Brain | [SLIM-Brain: A Data- and Training-Efficient Foundation Model for fMRI Data Analysis](https://arxiv.org/abs/2512.21881) | - |
| 2025 | arXiv | VIBE | [VIBE: Video-Input Brain Encoder for fMRI Response Modeling](https://arxiv.org/abs/2507.17958) | - |

#### Related: Scientific Domains

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [A small HER2 reader for routine H&E slides: real-world deployment](https://arxiv.org/abs/2610.40662) | [Code](https://huggingface.co/cloudkites/her2-reader) |
| 2026 | arXiv | CALIPER | [CALIPER: Clean Scenes Cannot Rank Physical Inference in Pretrained Visual Representations](https://arxiv.org/abs/2609.08250) | - |
| 2026 | arXiv | GEOPHYS | [GEOPHYS: The Geometry of Physical Plausibility](https://arxiv.org/abs/2606.20707) | - |
| 2026 | arXiv | HERA | [HERA: Historical Evidence Routing Adapter for Physical Prediction in Latent World Models](https://arxiv.org/abs/2608.05523) | - |
| 2026 | ECCV | - | [Human-Level Accuracy, Non-Human Strategies: Revealing Model-Human Divergence in Video Physical Reasoning](https://arxiv.org/abs/2609.22788) | [Code](https://github.com/fanhong-li/model-human-divergence) |
| 2026 | arXiv | IMPLY | [IMPLY: Physically Anchored Consistency for World-Model Rollouts](https://arxiv.org/abs/2609.12441) | - |
| 2026 | arXiv | - | [Readable Is Not Steerable: Pre-Registered Tests of Physical Structure in Learned Fluid Representations](https://arxiv.org/abs/2611.05577) | [Code](https://github.com/2025eb1100268-tech/readable-not-steerable) |
| 2026 | arXiv | - | [Variational Streaming Flow: Probabilistic Forecasting in Physical Time](https://arxiv.org/abs/2610.00976) | - |
| 2025 | arXiv | Opinion | [Opinion: Learning Intuitive Physics May Require More than Visual Data](https://arxiv.org/abs/2512.06232) | - |
| 2025 | arXiv | - | [The Platonic Universe: Do Foundation Models See the Same Sky?](https://arxiv.org/abs/2509.19453) | [Code](https://github.com/UniverseTBD/platonic-universe) |
| 2024 | arXiv | - | [Biology-inspired joint distribution neurons based on Hierarchical Correlation Reconstruction allowing for multidirectional propagation of values and densities](https://arxiv.org/abs/2405.05097) | - |

#### Related: Remote Sensing

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | ICPR | - | [Enhancing Foundation Models for Imbalanced SAR Ship Classification via Targeted Oversampling](https://arxiv.org/abs/2609.31657) | - |
| 2026 | arXiv | SAR2Agri | [SAR2Agri: Learning SAR Intensity Representations for Agricultural Monitoring](https://arxiv.org/abs/2608.11142) | - |
| 2026 | arXiv | SpectralEarth-FM | [SpectralEarth-FM: Bringing Hyperspectral Imagery into Multimodal Earth Observation Pretraining](https://arxiv.org/abs/2605.21075) | - |
| 2025 | arXiv | - | [DINOv3 as a Frozen Encoder for CRPS-Oriented Probabilistic Rainfall Nowcasting](https://arxiv.org/abs/2511.10894) | - |
| 2025 | arXiv | SpecBPP | [SpecBPP: A Self-Supervised Learning Approach for Hyperspectral Representation and Soil Organic Carbon Estimation](https://arxiv.org/abs/2507.19781) | - |

#### Related: Audio, Speech and Music

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | ISMIR | AllMusicCaps | [AllMusicCaps: Album Reviews as Complementary Supervision for Music CLAP](https://arxiv.org/abs/2608.25244) | [Code](https://github.com/MTG/allmusiccaps) |
| 2026 | arXiv | PairAlign | [PairAlign: A Framework for Autoregressive Tokenization via Self-Alignment with Applications to Audio Tokenization](https://arxiv.org/abs/2605.06582) | - |
| 2026 | arXiv | - | [Predictive audio representations for early detection and tracking of hidden dynamic objects](https://arxiv.org/abs/2609.13595) | - |
| 2025 | arXiv | - | [Foley Control: Aligning a Frozen Latent Text-to-Audio Model to Video](https://arxiv.org/abs/2510.21581) | [Project](https://stability-ai.github.io/foleycontrol.github.io/) |

#### Related: Language and Reasoning

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models](https://arxiv.org/abs/2607.12962) | - |
| 2026 | arXiv | - | [From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond](https://arxiv.org/abs/2606.28127) | - |
| 2026 | arXiv | GazeQwen | [GazeQwen: Lightweight Gaze-Conditioned LLM Modulation for Streaming Video Understanding](https://arxiv.org/abs/2603.25841) | [Code](https://github.com/phamtrongthang123/gazeqwen) |
| 2026 | arXiv | - | [One Latent, Many Tokens: Jointly Learning Compressed Embeddings for Efficient Language Diffusion](https://arxiv.org/abs/2609.33698) | [Code](https://github.com/infiniteYuanyl/JPEG-DLM) |
| 2026 | arXiv | - | [Parallelizable Probabilistic Latent Reasoning for Diverse Reasoning Trajectories](https://arxiv.org/abs/2610.29385) | - |

#### Related: Time Series, Tabular and Trajectories

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [Cross-Domain Joint-Embedding Pretraining For Heterogeneous Industrial Time Series](https://arxiv.org/abs/2611.02489) | - |
| 2026 | ICML | HEPA | [HEPA: A Self-Supervised Horizon-Conditioned Event Predictive Architecture for Time Series](https://arxiv.org/abs/2605.11130) | [Code](https://github.com/Forgis-Labs/HEPA) |
| 2026 | arXiv | - | [Revisiting Energy-based Tabular Anomaly Detection: Energy and Reconstruction are Complementary](https://arxiv.org/abs/2608.14186) | - |
| 2026 | arXiv | TEX-MEX | [TEX-MEX: Similarity-Guided Temporal Contrastive Learning for Time Series](https://arxiv.org/abs/2610.19557) | - |
| 2025 | arXiv | - | [Time to Embed: Unlocking Foundation Models for Time Series with Channel Descriptions](https://arxiv.org/abs/2505.14543) | - |

#### Related: Wireless, Networks and Security

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [A Wireless World Model for AI-Native 6G Networks](https://arxiv.org/abs/2603.25216) | - |
| 2026 | arXiv | AngularWM | [AngularWM: Wireless World Modeling for AoA Prediction from Multi-Antenna I/Q](https://arxiv.org/abs/2610.05543) | - |
| 2026 | arXiv | - | [Communication-Aware and Safety-Aware UAV Control via Predictive Latent Models](https://arxiv.org/abs/2607.00288) | - |
| 2026 | arXiv | - | [Emergent Compositional Communication for Latent World Properties](https://arxiv.org/abs/2604.03266) | [Code](https://github.com/TomekKaszynski/emergent-physics-comm) |
| 2026 | arXiv | - | [Opportunities of Self Supervised Learning for GNSS: Evaluation of a Deep Learning-Enhanced PVT Algorithm](https://arxiv.org/abs/2608.25674) | - |
| 2026 | ICC | - | [Structured Latent Dynamics in Wireless CSI via Homomorphic World Models](https://arxiv.org/abs/2603.20048) | - |
| 2026 | arXiv | WiSPER | [WiSPER: Pose-Supervised Predictive and Residual Flow Refinement For Multi-Person 3D Pose Estimation With WiFi CSI](https://arxiv.org/abs/2610.07025) | - |

## Background Cited in the Survey

Foundational work on self-supervised learning, world models, benchmarks and baselines that the survey builds on.

| Year | Venue | Acronym | Paper Title | Code/Project |
|:----:|:-----:|:-------:|:------------|:------------:|
| 2026 | arXiv | - | [Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence](https://arxiv.org/abs/2609.29669) | - |
| 2026 | NeurIPS | - | Joint-Embedding vs Reconstruction: Provable Benefits of Latent Space Prediction for Self-Supervised Learning | - |
| 2026 | ACM Computing Surveys | - | [Understanding World or Predicting Future? A Comprehensive Survey of World Models](https://doi.org/10.1145/3746449) | - |
| 2026 | arXiv | - | [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090) | - |
| 2026 | arXiv | - | [World-Action Models for Robot Learning and Control: A Survey](https://arxiv.org/abs/2609.16074) | - |
| 2026 | arXiv | WorldArena | [WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](https://arxiv.org/abs/2602.08971) | - |
| 2025 | arXiv | - | [A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732) | - |
| 2025 | arXiv | - | [Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) | - |
| 2025 | IJRR | - | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | - |
| 2025 | ICML | DINO-WM | [DINO-WM: World Models on Pre-trained Visual Features Enable Zero-shot Planning](https://proceedings.mlr.press/v267/zhou25t.html) | - |
| 2025 | arXiv | - | [Intuitive physics understanding emerges from self-supervised pretraining on natural videos](https://arxiv.org/abs/2502.11831) | - |
| 2025 | Nature | - | [Mastering Diverse Control Tasks through World Models](https://doi.org/10.1038/s41586-025-08744-2) | - |
| 2025 | CVPR | - | Navigation World Models | - |
| 2025 | ICLR | OGBench | OGBench: Benchmarking Offline Goal-Conditioned RL | - |
| 2025 | arXiv | - | [Perception Encoder: The best visual embeddings are not at the output of the network](https://arxiv.org/abs/2504.13181) | - |
| 2025 | arXiv | SigLIP 2 | [SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](https://arxiv.org/abs/2502.14786) | - |
| 2025 | CoRL | - | [Stress-Testing Offline Reward-Free Reinforcement Learning: A Case for Planning with Latent Dynamics Models](https://openreview.net/forum?id=jON7H6A9UU) | - |
| 2024 | CVPR | - | Can't Make an Omelette Without Breaking Some Eggs: Plausible Action Anticipation Using Large Video-Language Models | - |
| 2024 | IJCV | - | Context Autoencoder for Self-Supervised Representation Learning | - |
| 2024 | NeurIPS | - | Diffusion for World Modeling: Visual Details Matter in Atari | - |
| 2024 | NeurIPS | - | Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion | - |
| 2024 | TMLR | DINOv2 | DINOv2: Learning Robust Visual Features without Supervision | - |
| 2024 | Image and Vision Computing | EVA-02 | EVA-02: A Visual Representation for Neon Genesis | - |
| 2024 | ICML | Genie | Genie: Generative Interactive Environments | - |
| 2024 | WACV | - | Interaction Region Visual Transformer for Egocentric Action Anticipation | - |
| 2024 | ECCV | InternVideo2 | InternVideo2: Scaling Foundation Models for Multimodal Video Understanding | - |
| 2024 | arXiv | - | [Learning by Reconstruction Produces Uninformative Features For Perception](https://arxiv.org/abs/2402.11337) | - |
| 2024 | ICLR | - | Learning Interactive Real-World Simulators | - |
| 2024 | World Scientific Annual Review of AI | - | Masked Autoencoders for 3D Point Cloud Self-Supervised Learning | - |
| 2024 | ICRA | - | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | - |
| 2024 | ICLR | TD-MPC2 | TD-MPC2: Scalable, Robust World Models for Continuous Control | - |
| 2024 | arXiv | - | [World Models for Autonomous Driving: An Initial Survey](https://arxiv.org/abs/2403.02622) | - |
| 2023 | ICLR | - | Autoencoders as Cross-Modal Teachers: Can Pretrained 2D Image Transformers Help 3D Representation Learning? | - |
| 2023 | ICML | BLIP-2 | BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models | - |
| 2023 | ICML | - | Contrast with Reconstruct: Contrastive 3D Representation Learning Guided by Generative Pretraining | - |
| 2023 | CVPR | EVA | EVA: Exploring the Limits of Masked Visual Representation Learning at Scale | - |
| 2023 | arXiv | GAIA-1 | [GAIA-1: A Generative World Model for Autonomous Driving](https://arxiv.org/abs/2309.17080) | - |
| 2023 | CVPR | - | Image as a Foreign Language: BEiT Pretraining for Vision and Vision-Language Tasks | - |
| 2023 | CVPR | ImageBind | ImageBind: One Embedding Space To Bind Them All | - |
| 2023 | arXiv | - | [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705) | - |
| 2023 | Science | - | Learning Skillful Medium-Range Global Weather Forecasting | - |
| 2023 | arXiv | - | [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) | - |
| 2023 | AAAI | PeCo | PeCo: Perceptual Codebook for BERT Pre-training of Vision Transformers | - |
| 2023 | GCPR | - | Point2Vec for Self-Supervised Representation Learning on Point Clouds | - |
| 2023 | arXiv | RT-2 | [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) | - |
| 2023 | ICCV | - | Segment Anything | - |
| 2023 | ICLR | - | Transformers are Sample-Efficient World Models | - |
| 2023 | EMNLP | Video-LLaMA | Video-LLaMA: An Instruction-Tuned Audio-Visual Language Model for Video Understanding | - |
| 2023 | CVPR | VideoMAE V2 | VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking | - |
| 2023 | arXiv | ViNT | [ViNT: A Foundation Model for Visual Navigation](https://arxiv.org/abs/2306.14846) | - |
| 2023 | NeurIPS | - | Visual Instruction Tuning | - |
| 2023 | IEEE TAI | - | World Models for Reinforcement Learning: A Survey | - |
| 2022 | CVPR | - | A ConvNet for the 2020s | - |
| 2022 | OpenReview | - | [A Path Towards Autonomous Machine Intelligence, Version 0.9.2](https://openreview.net/forum?id=BZ5a1r-kVsf) | - |
| 2022 | ICLR | BEiT | BEiT: BERT Pre-Training of Image Transformers | - |
| 2022 | ICML | BLIP | BLIP: Bootstrapping Language-Image Pre-Training for Unified Vision-Language Understanding and Generation | - |
| 2022 | CoRL | CLIPort | CLIPort: What and Where Pathways for Robotic Manipulation | - |
| 2022 | ICLR | - | Conditional Object-Centric Learning from Video | - |
| 2022 | ICML | data2vec | data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language | - |
| 2022 | arXiv | - | [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) | - |
| 2022 | NeurIPS | Flamingo | Flamingo: A Visual Language Model for Few-Shot Learning | - |
| 2022 | ICLR | iBOT | iBOT: Image BERT Pre-Training with Online Tokenizer | - |
| 2022 | CVPR | - | Masked Autoencoders Are Scalable Vision Learners | - |
| 2022 | CVPR | - | Masked Feature Prediction for Self-Supervised Visual Pre-Training | - |
| 2022 | ECCV | MultiMAE | [MultiMAE: Multi-modal Multi-task Masked Autoencoders](https://doi.org/10.1007/978-3-031-19836-6_20) | - |
| 2022 | CVPR | MViTv2 | MViTv2: Improved Multiscale Vision Transformers for Classification and Detection | - |
| 2022 | CVPR | Point-BERT | Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling | - |
| 2022 | NeurIPS | Point-M2AE | Point-M2AE: Multi-scale Masked Autoencoders for Hierarchical Point Cloud Pre-training | - |
| 2022 | CoRL | R3M | R3M: A Universal Visual Representation for Robot Manipulation | - |
| 2022 | IJCV | - | Rescaling Egocentric Vision: Collection, Pipeline and Challenges for EPIC-KITCHENS-100 | - |
| 2022 | CVPR | SimMIM | SimMIM: A Simple Framework for Masked Image Modeling | - |
| 2022 | arXiv | - | [Temporal Difference Learning for Model Predictive Control](https://arxiv.org/abs/2203.04955) | - |
| 2022 | ACM Computing Surveys | - | [Transformers in Vision: A Survey](https://doi.org/10.1145/3505244) | - |
| 2022 | ICLR | VICReg | [VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning](https://openreview.net/forum?id=xm6YD62D1Ub) | - |
| 2022 | CVPR | - | Video Swin Transformer | - |
| 2022 | NeurIPS | VideoMAE | VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training | - |
| 2021 | NeurIPS | - | Align before Fuse: Vision and Language Representation Learning with Momentum Distillation | - |
| 2021 | ICCV | - | An Empirical Study of Training Self-Supervised Vision Transformers | - |
| 2021 | NeurIPS | - | Decision Transformer: Reinforcement Learning via Sequence Modeling | - |
| 2021 | ICML | - | E(n) Equivariant Graph Neural Networks | - |
| 2021 | ICCV | - | Emerging Properties in Self-Supervised Vision Transformers | - |
| 2021 | CVPR | - | Exploring Simple Siamese Representation Learning | - |
| 2021 | ICML | - | Is Space-Time Attention All You Need for Video Understanding? | - |
| 2021 | Nature Machine Intelligence | - | Learning Nonlinear Operators via DeepONet Based on the Universal Approximation Theorem of Operators | - |
| 2021 | ICML | - | Learning Transferable Visual Models From Natural Language Supervision | - |
| 2021 | ICLR | - | [Mastering Atari with Discrete World Models](https://openreview.net/forum?id=0oabwyZbOu) | - |
| 2021 | NeurIPS | - | Offline Reinforcement Learning as One Big Sequence Modeling Problem | - |
| 2021 | arXiv | - | [Offline Reinforcement Learning with Implicit Q-Learning](https://arxiv.org/abs/2110.06169) | - |
| 2021 | arXiv | Perceiver IO | [Perceiver IO: A General Architecture for Structured Inputs and Outputs](https://arxiv.org/abs/2107.14795) | - |
| 2021 | ICML | Perceiver | Perceiver: General Perception with Iterative Attention | - |
| 2021 | ICCV | - | Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions | - |
| 2021 | ICML | - | Scaling Up Visual and Vision-Language Representation Learning with Noisy Text Supervision | - |
| 2021 | TPAMI | - | [Self-Supervised Visual Feature Learning With Deep Neural Networks: A Survey](https://doi.org/10.1109/tpami.2020.2992393) | - |
| 2021 | ICCV | - | Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows | - |
| 2021 | Proc. IEEE | - | [Toward Causal Representation Learning](https://doi.org/10.1109/jproc.2021.3058954) | - |
| 2021 | ICML | - | Training Data-Efficient Image Transformers & Distillation through Attention | - |
| 2021 | arXiv | - | [Understanding Dimensional Collapse in Contrastive Self-Supervised Learning](https://arxiv.org/abs/2110.09348) | - |
| 2021 | arXiv | VideoGPT | [VideoGPT: Video Generation Using VQ-VAE and Transformers](https://arxiv.org/abs/2104.10157) | - |
| 2021 | arXiv | VIMPAC | [VIMPAC: Video Pre-Training via Masked Token Prediction and Contrastive Learning](https://arxiv.org/abs/2106.11250) | - |
| 2021 | ICCV | ViViT | ViViT: A Video Vision Transformer | - |
| 2020 | ICML | - | A Simple Framework for Contrastive Learning of Visual Representations | - |
| 2020 | arXiv | - | [An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) | - |
| 2020 | NeurIPS | - | [Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning](https://proceedings.neurips.cc/paper/2020/hash/f3ada80d5c4ee70142b17b8192b2958e-Abstract.html) | - |
| 2020 | NeurIPS | - | Conservative Q-Learning for Offline Reinforcement Learning | - |
| 2020 | arXiv | D4RL | [D4RL: Datasets for Deep Data-Driven Reinforcement Learning](https://arxiv.org/abs/2004.07219) | - |
| 2020 | ICML | - | Data-Efficient Image Recognition with Contrastive Predictive Coding | - |
| 2020 | ICLR | - | Data-Efficient Reinforcement Learning with Self-Predictive Representations | - |
| 2020 | NeurIPS | - | Denoising Diffusion Probabilistic Models | - |
| 2020 | ICLR | - | Dream to Control: Learning Behaviors by Latent Imagination | - |
| 2020 | CACM | - | Green AI | - |
| 2020 | arXiv | - | [Improved Baselines with Momentum Contrastive Learning](https://arxiv.org/abs/2003.04297) | - |
| 2020 | NeurIPS | - | Language Models are Few-Shot Learners | - |
| 2020 | ICML | - | Learning to Simulate Complex Physics with Graph Networks | - |
| 2020 | Annu. Rev. Fluid Mech. | - | Machine Learning for Fluid Mechanics | - |
| 2020 | Nature | - | [Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model](https://doi.org/10.1038/s41586-020-03051-4) | - |
| 2020 | CVPR | - | Momentum Contrast for Unsupervised Visual Representation Learning | - |
| 2020 | NeurIPS | - | Object-Centric Learning with Slot Attention | - |
| 2020 | CVPR | - | Self-Supervised Learning of Pretext-Invariant Representations | - |
| 2020 | NeurIPS | - | Unsupervised Learning of Visual Features by Contrasting Cluster Assignments | - |
| 2019 | ICLR | - | Learning Deep Representations by Mutual Information Estimation and Maximization | - |
| 2019 | ICML | - | [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) | - |
| 2019 | NeurIPS | - | Learning Representations by Maximizing Mutual Information Across Views | - |
| 2019 | arXiv | - | [Model-Based Reinforcement Learning for Atari](https://arxiv.org/abs/1903.00374) | - |
| 2019 | TPAMI | - | [Multimodal Machine Learning: A Survey and Taxonomy](https://doi.org/10.1109/tpami.2018.2798607) | - |
| 2019 | ICCV | - | Revisiting Point Cloud Classification: A New Benchmark Dataset and Classification Model on Real-World Data | - |
| 2019 | ICCV | - | SlowFast Networks for Video Recognition | - |
| 2019 | NeurIPS | - | When to Trust Your Model: Model-Based Policy Optimization | - |
| 2018 | ECCV | - | Deep Clustering for Unsupervised Learning of Visual Features | - |
| 2018 | NeurIPS | - | Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models | - |
| 2018 | arXiv | - | [DeepMind Control Suite](https://arxiv.org/abs/1801.00690) | - |
| 2018 | arXiv | - | [Representation Learning with Contrastive Predictive Coding](https://arxiv.org/abs/1807.03748) | - |
| 2018 | AAAI | - | [Safe Reinforcement Learning via Shielding](https://doi.org/10.1609/aaai.v32i1.11797) | - |
| 2018 | ICML | - | Stochastic Video Generation with a Learned Prior | - |
| 2018 | ICRA | - | Time-Contrastive Networks: Self-Supervised Learning from Video | - |
| 2018 | ECCV | - | Tracking Emerges by Colorizing Videos | - |
| 2018 | arXiv | - | [Unsupervised Representation Learning by Predicting Image Rotations](https://arxiv.org/abs/1803.07728) | - |
| 2018 | arXiv | - | [World Models](https://arxiv.org/abs/1803.10122) | - |
| 2017 | ICASSP | - | Audio Set: An Ontology and Human-Labeled Dataset for Audio Events | - |
| 2017 | Book | - | Elements of Causal Inference: Foundations and Learning Algorithms | - |
| 2017 | ICML | - | On Calibration of Modern Neural Networks | - |
| 2017 | CVPR | - | Scene Parsing Through ADE20K Dataset | - |
| 2017 | NeurIPS | - | Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles | - |
| 2017 | arXiv | - | [The 2017 DAVIS Challenge on Video Object Segmentation](https://arxiv.org/abs/1704.00675) | - |
| 2017 | arXiv | - | [The Kinetics Human Action Video Dataset](https://arxiv.org/abs/1705.06950) | - |
| 2017 | ICCV | - | The Something Something Video Database for Learning and Evaluating Visual Common Sense | - |
| 2016 | ACM TOG | - | A Scalable Active Framework for Region Annotation in 3D Shape Collections | - |
| 2016 | CVPR | - | Context Encoders: Feature Learning by Inpainting | - |
| 2015 | ICCV | - | Unsupervised Learning of Visual Representations using Videos | - |
| 2015 | ICCV | - | Unsupervised Visual Representation Learning by Context Prediction | - |
| 2014 | ECCV | Microsoft COCO | Microsoft COCO: Common Objects in Context | - |
| 2009 | Book | - | Causality | - |
| 2009 | CVPR | ImageNet | ImageNet: A Large-Scale Hierarchical Image Database | - |
| 2007 | JASA | - | Strictly Proper Scoring Rules, Prediction, and Estimation | - |
| 2004 | UAI | - | [Predictive State Representations: A New Theory for Modeling Dynamical Systems](https://arxiv.org/abs/1207.4167) | - |
| 2001 | NeurIPS | - | [Predictive Representations of State](https://proceedings.neurips.cc/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html) | - |
