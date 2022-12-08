# Wiener Filter General Notes

**Definitionen und Schlagwörter/sätze**

* Der Wiener Filter ist ein Filter zur Signalverarbeitung, bei der, gemessen an der mittleren quadratischen Abweichung,
eine optimale Rauschunterdrückung durchgeführt wird.
    * Voraussetzung: Das Signal und das addative Rauschen gleichen stochastischen Prozessen mit bekannter Spektralverteilung
      oder bekannter Autokorrelation und Kreuzkorrelation
    * Fehlerkriterium: Minimale mittlere quadratische Abweichung (https://de.wikipedia.org/wiki/Wiener-Filter)

* Bei der Signalverarbeitung ist der Wiener Filter ein Fiter, der verwendet wird, um eine Schätzung eines gewünschten 
oder zufälligen Zielprozesses durch lineare zeitinvariante (LTI) Filterung eines beobachteten verrauschten Prozesses
unter Annahme bekannter stationärer Signal- und Rauschspektren und additiven Rauschen zu erzeugen. Der Wiener Filter 
minimiert den mittleren quadratischen Fehler zwischen dem geschätzen Zufallsprozess und dem gewünschten Prozess.
  (https://de.wikibrief.org/wiki/Wiener_filter)

*  


## Existing Libraries for Wiener Filter

* ### **SciKit-Image Library** 

The skimage library is a collection of algorithms for image processing. 
There are two different methods with different parameters for applying the wiener filter on an image.
These methods are available within the submodule restoration.

* Wiener-Hunt deconvolution

```python
skimage.restoration.wiener(image, psf, balance, reg=None, is_real=True, clip=True)
```

* Unsupervised Wiener-Hunt deconvolution

```python
skimage.restoration.unsupervised_wiener(image, psf, reg=None, user_params=None, is_real=True, clip=True,*, random_state=None)
```

* ### **SciPy Library**


```python
scipy.signal.wiener(im, mysize=None, noise=None)
```