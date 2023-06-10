import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BarracaComponent } from './barraca/barraca.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [BarracaComponent],
  imports: [CommonModule, RouterModule],
  exports: [BarracaComponent],
})
export class BarracaModule {}
