import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { CadastroModule } from './pages/cadastro/cadastro.module';
import { FooterModule } from './pages/footer/footer.module';
import { HeaderModule } from './pages/header/header.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CadastroModule,
    FooterModule,
    HeaderModule,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
