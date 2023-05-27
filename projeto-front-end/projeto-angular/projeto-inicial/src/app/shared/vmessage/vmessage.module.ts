import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VmessageComponent } from './vmessage/vmessage.component';

@NgModule({
  declarations: [VmessageComponent],
  imports: [CommonModule],
  exports: [VmessageComponent],
})
export class VMessageModule {}
