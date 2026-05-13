# ASM2d-BSM2

`asm2dbsm2` is a Python package exposing compiled ASM2d-BSM2 plant-wide wastewater treatment model (Water and Slduge lines).

## Installation

```bash
pip install asm2dbsm2
```

## Import

```python
from asm2dbsm2 import 'Modules'
```

```python
from asm2dbsm2 import asm2d, combiner, combiner3, combiner4
from asm2dbsm2 import flowsplitter, hyddelay, settler1d
from asm2dbsm2 import adm1dae1, adm1dae2, adm1ode, adm2asm, asm2adm, carboncombiner, metalcombiner, ...
```

## Modules

- `adm1dae1` : ADM1 DAE1.
- `adm1dae2` : ADM1 DAE2.
- `adm1ode` : ADM1 ODEr.
- `adm2asm` : ADM-to-ASM2d interface.
- `asm2adm` : ASM2d-to-ADM interface.
- `asm2d` : ASM2d biological reactor.
- `carboncombiner` : External carbon combiner for ASM2d reactor.
- `combiner` : Two-stream ASM2d flow combiner.
- `combiner3` : Three-stream ASM2d flow combiner.
- `combiner4` : Four-stream ASM2d flow combiner.
- `combineradm1` : ADM1-specific combiner.
- `dae1combiner` : DAE1 ADM combiner.
- `dae2combiner` : DAE2 ADM combiner.
- `dewatering` : ASM2d dewatering unit.
- `flowsplitter` : ASM2d flow splitter.
- `hyddelay` : ASM2d hydraulic delay.
- `metalcombiner` : Metal dosing combiner for ASM2d.
- `pHdelay` : pH delay for ADM interfaces.
- `pHsolv` : pH solver for ADM DAE.
- `primclar` : ASM2d primary clarifier.
- `settler1d` : ASM2d 10-layer secondary settler.
- `sh2solv` : SH2 solver for ADM1 DAE2.
- `storage` : ASM2d reject-water storage tank.
- `storagebypass` : ASM2d storage bypass.
- `storagedelay` : ASM2d storage delay.
- `thickener` : ASM2d thickener.


## Python packaging / adaptation

- Package: `asm2dbsm2`
- Python packaging and ASM2d-BSM2 adaptation: Dr Taher Abunama


## Attribution and license

See `LICENSE` and `THIRD_PARTY_NOTICES.md`. 
Publications using this software should acknowledge the BSM2 sources and the upstream authors.
