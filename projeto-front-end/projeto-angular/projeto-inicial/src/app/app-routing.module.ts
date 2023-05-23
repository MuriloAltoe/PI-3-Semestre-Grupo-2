import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CadastroComponent } from './pages/cadastro/cadastro/cadastro.component';
import { HomeComponent } from './pages/home/home/home.component';
import { ContatoComponent } from './pages/contato/contato/contato.component';
import { SobreComponent } from './pages/sobre/sobre/sobre.component';


const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'home',
  },
  {
    path: 'home',
    component: HomeComponent
  },
  {
    path: 'cadastro',
    component: CadastroComponent,
  },
  {
    path: 'contato',
    component: ContatoComponent,
  },
  {
    path: 'sobre',
    component: SobreComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
