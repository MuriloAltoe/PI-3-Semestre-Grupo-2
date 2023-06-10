import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-barraca',
  templateUrl: './barraca.component.html',
  styleUrls: ['./barraca.component.scss']
})
export class BarracaComponent implements OnInit {

  @Input() produtor = 0;

  ngOnInit(): void {
  }

}
