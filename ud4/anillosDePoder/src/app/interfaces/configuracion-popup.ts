import { ButtonSeverity } from "primeng/button";

export interface ConfiguracionPopup {
    message: string;
    header?: string;
    nameButton: string;
    severity: ButtonSeverity;
    acceptLabel : string;
    rejectLabel : string;
    // pasar una función para ejecutar
    funcion: (messageService?: any) => void | Boolean;

}
