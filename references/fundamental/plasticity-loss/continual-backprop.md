# Continual Backprop: Stochastic Gradient Descent with Persistent Randomness — Dohare et al. 2021

**Paper:** Dohare, Mahmood, Sutton (2021)
**Title:** Continual Backprop: Stochastic Gradient Descent with Persistent Randomness
**Source:** arXiv 2108.06325 (August 2021)
**Category:** Fundamental — Plasticity Loss — Algorithm Design (Precursor)

---

## Problem

In continual learning, backpropagation performs well initially but its performance degrades over time. How can we modify backpropagation to maintain its effectiveness indefinitely?

## Method: Continual Backprop (CBP)

A modification of standard backpropagation that introduces **persistent randomness**:
- After each training step, a small number of hidden units are **randomly reinitialized**
- Selection based on a **utility measure** — units contributing least to the network's output
- Incoming and outgoing weights of selected units are reset to random initialization values
- The utility of a unit is measured by the magnitude of its contribution (activation × outgoing weight)

## Key Design Choices

1. **Replacement rate**: Fraction of units replaced per step (hyperparameter, typically small ~0.001)
2. **Utility metric**: Contribution-based measure to identify least useful units
3. **Maturity threshold**: New units need a grace period before being eligible for replacement
4. **Weight initialization**: Replaced units use the same initialization distribution as at network creation

## Core Insight

Standard backpropagation has **no mechanism for injecting new diversity** once the network settles. Over time:
- Units become increasingly specialized and interdependent
- The "search space" of effective gradient updates narrows
- Network loses capacity for novel feature discovery

CBP maintains an "exploration budget" — a fraction of the network is always in a fresh, randomly initialized state, ready to discover new features.

## Critical Insight for Sparse Topology Research

CBP is essentially a **crude form of dynamic topology** operating at the unit level:
- It "removes" low-utility units and "adds" fresh ones
- This is functionally similar to sparse topology evolution but coarser-grained
- A sparse topology approach could achieve the same effect more efficiently by operating at the connection level
- The utility metric concept directly transfers to sparse topology methods (e.g., magnitude-based pruning)

## Relation to Other Work

- Evolved into: Dohare et al. 2024 (Nature paper — full validation)
- Parallel approach: Nikishin et al. 2022/2023 (periodic resets / plasticity injection in RL)
- Theoretical basis: Lyle et al. 2023 (why this works — maintains curvature diversity)
