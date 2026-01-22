import { Routes } from '@angular/router';
import { Detalle } from './anillo/detalle/detalle';
import { Busqueda } from './anillo/busqueda/busqueda';
import { DetalleRaza } from './raza/detalle-raza/detalle-raza';
import { BusquedaRaza } from './raza/busqueda-raza/busqueda-raza';
import { FormularioRaza } from './raza/formulario-raza/formulario-raza';
import { FormularioAnillo } from './anillo/formulario-anillo/formulario-anillo';
import { BuscarPersonaje } from './personajes/buscar-personaje/buscar-personaje';
import { DetallePersonaje } from './personajes/detalle-personaje/detalle-personaje';


export const routes: Routes = [
    { path: 'detalle', component: Detalle },
    { path: 'buscar', component: Busqueda },
    { path: 'detalle-raza', component: DetalleRaza },
    { path: 'buscar-raza', component: BusquedaRaza },
    { path: 'crear-raza', component: FormularioRaza },
    { path: 'crear-anillo', component: FormularioAnillo },
    { path: 'personajes', component: BuscarPersonaje },
    { path: 'editar/:id', component: DetallePersonaje },
    { path: 'crear-personaje', component: DetallePersonaje },
];
