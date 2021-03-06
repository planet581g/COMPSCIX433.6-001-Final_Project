# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:30:17 2016

@author: Eric
"""
import numpy as np
import numpy.linalg as LA


def mean_vector(X, rescale=0):
    """Given a matrix, return the mean adjusted matrix and mean vector."""
    μ = np.mean(X, axis=0)  # this is the mean vector
    if rescale == 1:
        sigma = np.std(X, axis=0)
    else:
        sigma = 1
    Z = (X - μ) / sigma
    return(Z, μ, sigma)


def pca_manual(X, rescale=0):
    Z, μ, sigma = mean_vector(X, rescale)
    C = np.cov(Z, rowvar=False)
    [λ, V] = LA.eigh(C)
    λ = np.flipud(λ)
    V = np.flipud(np.transpose(V))
    P = np.dot(Z, V.T)
    return (P, V, μ, λ, sigma)


def Xrec(P, V, μ, n=1):
    R = (np.dot(P[:, 0: n], V[0: n, :]))
    Xrec = R + μ
    return Xrec


def calculate_variance(λ):
    var_plot = np.zeros(len(λ))
    lam_sum = 0
    sum_eigv = np.sum(λ)
    for i, lam in enumerate(λ):
        lam_sum = lam + lam_sum
        var_plot[i] = 100 * (lam_sum / sum_eigv)
    return var_plot
