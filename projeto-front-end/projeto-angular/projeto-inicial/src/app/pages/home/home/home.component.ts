import { Component, OnInit } from '@angular/core';
import { UsuarioService } from 'src/app/core/services/usuario/usuario.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {

  constructor(private service: UsuarioService) {}

  ngOnInit(): void {
    this.service.getAllUser().subscribe({
      next: (user) => {
        console.log(user);
      },
      error: (err) => console.error(err),
    });
  }

}
