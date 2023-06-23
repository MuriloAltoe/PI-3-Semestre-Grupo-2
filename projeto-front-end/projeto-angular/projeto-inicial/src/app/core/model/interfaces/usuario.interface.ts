import { IItem } from "./item.interface";

export interface IUsuario {
  _id: string;
  nome: string;
  email: string;
  senha: string;
  tipo: string;
  cep: string;
  rua: string;
  numero: number;
  bairro: string;
  cidade: string;
  estado: string;
  complemento: string;
  entrega: boolean;
  telefone: string;
  itens: IItem[];
}
