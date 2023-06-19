import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { INewItem } from '../../model/interfaces/novo-item.interface';
import { Observable } from 'rxjs';
import { IItem } from '../../model/interfaces/item.interface';

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {
  
  private readonly url = environment.urlApi;

  constructor(private httpclient: HttpClient) {}

  creatItem(item: INewItem): Observable<IItem>{
    return this.httpclient.post<IItem>(`${this.url}item`, item);
  }

  updateItem(id: string, item: IItem): Observable<IItem>{
    return this.httpclient.put<IItem>(`${this.url}item/${id}`, item);
  }

  deleteItem(id: string): Observable<any>{
    return this.httpclient.delete<any>(`${this.url}item/${id}`);
  }
}
