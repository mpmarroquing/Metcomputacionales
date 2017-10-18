import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
from scipy.signal import convolve2d

#para la imagen 1

Im1 = plt.imread("20_popc_cho009-1.tif")

plt.imshow(Im1[:,:], cmap = plt.cm.Greys_r)
plt.title('Imagen1 Original', fontsize=12)
plt.show()
plt.close()


#dejar las frecuencias bajas
t = np.linspace(-10, 10, 20)
bump = np.exp(-0.005*t**2)
bump = bump / np.trapz(bump)

kernel = bump[:, np.newaxis] * bump[np.newaxis, :]


kernel_ft = fftpack.fft2(kernel, shape=Im1.shape[:2], axes=(0, 1))

im1_ft = fftpack.fft2(Im1, axes=(0, 1))
im1_2_ft = kernel_ft[:, :] * im1_ft
im1_2 = fftpack.ifft2(im1_2_ft, axes=(0, 1)).real


plt.imshow(im1_2[:,:], cmap = plt.cm.Greys_r)
plt.title('Imagen1 pasa bajas', fontsize=12)
plt.show()


#dejar las frecuencias altas

t = np.linspace(-10, 10, 20)
bump = 1-np.exp(-0.005*t**2)
bump = bump / np.trapz(bump)

kernel = bump[:, np.newaxis] * bump[np.newaxis, :]


kernel_ft = fftpack.fft2(kernel, shape=Im1.shape[:2], axes=(0, 1))

im1_ft = fftpack.fft2(Im1, axes=(0, 1))
im1_2_ft = kernel_ft[:, :] * im1_ft
im1_2 = fftpack.ifft2(im1_2_ft, axes=(0, 1)).real


plt.imshow(im1_2[:,:], cmap = plt.cm.Greys_r)
plt.title('Imagen1 pasa altas', fontsize=12)
plt.show()

#para la imagen 2
Im2 = plt.imread("colesterol-1.tif")
plt.imshow(Im2[:,:], cmap = plt.cm.Greys_r)
plt.title('Imagen2 Original', fontsize=12)
plt.show()
plt.close()


#dejar las frecuencias bajas
t = np.linspace(-10, 10, 20)
bump = np.exp(-0.005*t**2)
bump = bump / np.trapz(bump)

kernel = bump[:, np.newaxis] * bump[np.newaxis, :]


kernel_ft = fftpack.fft2(kernel, shape=Im2.shape[:2], axes=(0, 1))

im2_ft = fftpack.fft2(Im2, axes=(0, 1))
im2_2_ft = kernel_ft[:, :] * im2_ft
im2_2 = fftpack.ifft2(im2_2_ft, axes=(0, 1)).real


plt.imshow(im2_2[:,:], cmap = plt.cm.Greys_r)
plt.title('Imagen2 pasa bajas', fontsize=12)
plt.show()


#dejar las frecuencias altas

t = np.linspace(-10, 10, 20)
bump = 1-np.exp(-0.005*t**2)
bump = bump / np.trapz(bump)

kernel = bump[:, np.newaxis] * bump[np.newaxis, :]


kernel_ft = fftpack.fft2(kernel, shape=Im2.shape[:2], axes=(0, 1))

im2_ft = fftpack.fft2(Im2, axes=(0, 1))
im2_2_ft = kernel_ft[:, :] * im2_ft
im2_2 = fftpack.ifft2(im2_2_ft, axes=(0, 1)).real


plt.imshow(im2_2[:,:], cmap = plt.cm.Greys_r)
plt.title('Imagen2 pasa altas', fontsize=12)
plt.show()

#para la imagen 3
Im3 = plt.imread("ves_full_150_002-1.tif")
plt.imshow(Im3[:,:], cmap = plt.cm.Greys_r)
plt.title('Imagen3 Original', fontsize=12)
plt.show()
plt.close()


#dejar las frecuencias bajas
t = np.linspace(-10, 10, 20)
bump = np.exp(-0.005*t**2)
bump = bump / np.trapz(bump)

kernel = bump[:, np.newaxis] * bump[np.newaxis, :]

kernel_ft = fftpack.fft2(kernel, shape=Im3.shape[:2], axes=(0, 1))

im3_ft = fftpack.fft2(Im3, axes=(0, 1))
im3_2_ft = kernel_ft[:, :] * im3_ft
im3_2 = fftpack.ifft2(im3_2_ft, axes=(0, 1)).real


plt.imshow(im3_2[:,:], cmap = plt.cm.Greys_r)
plt.title('Imagen3 pasa bajas', fontsize=12)
plt.show()


#dejar las frecuencias altas

t = np.linspace(-10, 10, 20)
bump = 1-np.exp(-0.005*t**2)
bump = bump / np.trapz(bump)

kernel = bump[:, np.newaxis] * bump[np.newaxis, :]

kernel_ft = fftpack.fft2(kernel, shape=Im3.shape[:2], axes=(0, 1))

im3_ft = fftpack.fft2(Im3, axes=(0, 1))
im3_2_ft = kernel_ft[:, :] * im3_ft
im3_2 = fftpack.ifft2(im3_2_ft, axes=(0, 1)).real


plt.imshow(im3_2[:,:], cmap = plt.cm.Greys_r)
plt.title('Imagen3 pasa altas', fontsize=12)
plt.show()
