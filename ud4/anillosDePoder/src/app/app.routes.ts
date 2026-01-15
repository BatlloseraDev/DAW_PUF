import { Routes } from '@angular/router';
import { Detalle } from './anillo/detalle/detalle';
import { Busqueda } from './anillo/busqueda/busqueda';
import { DetalleRaza } from './raza/detalle-raza/detalle-raza';
import { BusquedaRaza } from './raza/busqueda-raza/busqueda-raza';
import { FormularioRaza } from './raza/formulario-raza/formulario-raza';
import { FormularioAnillo } from './anillo/formulario-anillo/formulario-anillo';


export const routes: Routes = [
    { path: 'detalle', component: Detalle },
    { path: 'buscar', component: Busqueda },
    { path: 'detalle-raza', component: DetalleRaza },
    { path: 'buscar-raza', component: BusquedaRaza },
    { path: 'crear-raza', component: FormularioRaza },
    { path: 'crear-anillo', component: FormularioAnillo}
];
