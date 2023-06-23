import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PerfilBarracaComponent } from './perfil-barraca/perfil-barraca.component';
import { FormsModule } from '@angular/forms';
import { VMessageModule } from 'src/app/shared/vmessage/vmessage.module';
import { RouterModule } from '@angular/router';



@NgModule({
  declarations: [
    PerfilBarracaComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    VMessageModule,
    RouterModule
  ],
  exports: [
    PerfilBarracaComponent
  ]
})
export class PerfilBarracaModule { }
