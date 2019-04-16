# Rapid Characterisation Protocols for Patch-Clamp Electrophysiology

Collection of protocols for rapid characterisation of ion channel kinetics.

Here we have provided plain text `.txt` and comma-separated-value `.csv` formats.

`.atf` files are also provided and are intended to be used with the Axon pClamp software.

Some also support `.eph` files which are intended to be used with the Nanion SyncroPatch software.

## Staircase voltage clamp for hERG/IKr measurements
The protocol `staircase-ramp` is a short, high information-content voltage clamp protocol that is applicable in _automated high-throughput patch clamp systems_.
The protocol and its application have a dedicated [Github repository](https://github.com/CardiacModelling/hERGRapidCharacterisation)).

## Sinusoidal voltage clamp for hERG/IKr measurements
The protocol `sinewave-ramp` is a slightly-updated version of the sinusoidal voltage clamp we first published in 2018 (which has a dedicated [Github repository](http://www.github.com/mirams/sine-wave)).
The update here is a ramp during the initial 'leak step' rather than a fixed potential.


# Format/Units

Each file has two columns, the first one is time (in [seconds]) and the second column is voltage (in [milliVolts]).


# Acknowledging this work

If you publish any work based on the contents of this repository please cite:

Lei, C. L., Clerx, M., Gavaghan, D. J., Polonchuk, L., Mirams, G. R., Wang, K.
(2019).
[Rapid characterisation of hERG channel kinetics I: using an automated high-throughput system](https://doi.org/10.1101/609727).
_bioRxiv_, 609727.

Beattie, K. A., Hill, A. P., Bardenet, R., Cui, Y., Vandenberg, J. I., Gavaghan, D. J., de Boer, T. P. & Mirams, G. R.
(2018).
[Sinusoidal voltage protocols for rapid characterisation of ion channel kinetics](https://doi.org/10.1113/JP275733).
_J. Physiol._ 596, 1813–1828.

