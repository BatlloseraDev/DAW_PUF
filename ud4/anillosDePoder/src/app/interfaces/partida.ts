export interface PreguntaEstado {
    id: number;
    respuesta: number |null;
}


export interface Partida {
    id: number;
    preguntas: PreguntaEstado[];
    numeroCorrectas: number;
    acabada: boolean;
    perdida: boolean;
}

export interface PartidaDTO {
    id: number;
    fechaInicio: string;
    fechaFin: string |null;
    numeroCorrectas: number;
    finPartida: boolean;
}

export interface RespuestaDTO {
    id: number;
    pregunta: string;
    respuesta1: string;
    respuesta2: string;
    respuesta3: string;
    respuesta4: string;
    correcta: number | null;
}