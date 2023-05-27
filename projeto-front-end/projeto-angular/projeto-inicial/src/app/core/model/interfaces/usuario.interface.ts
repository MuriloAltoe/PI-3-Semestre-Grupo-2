export interface IUsuario {
  user_id: number;
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
}
