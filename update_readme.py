readme_content = """# Quantum Transformer AI v4.1
### *A Hybrid Quantum-Classical Architecture for Intelligent Classification*

---

## Executive Summary

This project represents a **significant foray into the vanguard of computational intelligence** — the deliberate and principled fusion of quantum mechanical phenomena with classical deep learning paradigms. What has been constructed here is not a superficial wrapper around existing tools, but a **ground-up architected Quantum Transformer** — a system that harnesses the probabilistic nature of quantum states to perform attention-based reasoning in ways that classical silicon cannot replicate.

---

## The Philosophy of Construction

Modern artificial intelligence is approaching a fundamental ceiling. Classical neural networks, however deep or wide, are ultimately bound by the deterministic flow of electrons through transistors. **Quantum computing offers a genuinely different computational substrate** — one where information exists in superposition, where entanglement creates non-local correlations, and where measurement collapses probability amplitudes into meaningful signals.

The central thesis of this project is provocative and deliberate:

> *"What if the attention mechanism at the heart of the Transformer architecture — the engine behind GPT, BERT, and every modern language model — could be reimagined through the lens of quantum mechanics?"*

This is precisely what has been built.

---

## Architectural Deep Dive

### I. The Quantum Attention Mechanism

At the core of this system lies a **bespoke Quantum Attention Head** — a parameterised quantum circuit that computes attention-like correlations between encoded quantum states.

Classical Transformer attention computes:

$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V$$

Our quantum analog replaces this with a **physically motivated entanglement protocol:**

- **Query states** are amplitude-encoded into the first half of the qubit register using parameterised RY and RZ rotations
- **Key states** are encoded into the second half of the register
- **CNOT entanglement layers** create genuine quantum correlations between query and key qubits
- **Reverse entanglement** extracts the attention score through measurement of Pauli-Z expectation values

This is not a simulation of attention. This is **attention reimagined as a quantum interference phenomenon.**

---

### II. Data Re-Uploading for Universal Approximation

The **Quantum Value Circuit** implements a cutting-edge technique from quantum machine learning theory known as **data re-uploading** — a protocol proven to grant quantum circuits the capacity for universal function approximation.

Rather than encoding data once and processing it, the circuit:

1. Encodes the value vector with **learnable scaling parameters** — allowing the model to discover the optimal encoding magnitude autonomously
2. Applies a full variational layer of RX, RY, RZ rotations with trainable parameters
3. Creates entanglement through a **rotating CNOT ladder** — alternating offset patterns that maximise qubit connectivity
4. **Re-uploads the original data** at intermediate layers, reinforcing the signal against quantum decoherence effects

Measurements are taken in **two complementary bases** — the computational Z basis and the X basis — extracting maximal classical information from the quantum state.

---

### III. Multi-Head Quantum Attention

Drawing direct inspiration from the multi-head attention of the original **Attention Is All You Need** paper (Vaswani et al., 2017), this architecture deploys **parallel quantum attention heads**, each learning orthogonal representations of the input space.

Each head maintains its own:
- Quantum attention weight tensor
- Quantum value weight tensor
- Learnable encoding scale vector

The outputs of all heads are concatenated and projected back to the embedding dimension — forcing the model to **synthesise quantum information from multiple perspectives simultaneously.**

---

### IV. The Transformer Block - Quantum Style
