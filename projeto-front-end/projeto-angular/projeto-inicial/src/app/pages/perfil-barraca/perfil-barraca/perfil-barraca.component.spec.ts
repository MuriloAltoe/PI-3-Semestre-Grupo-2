import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PerfilBarracaComponent } from './perfil-barraca.component';

describe('PerfilBarracaComponent', () => {
  let component: PerfilBarracaComponent;
  let fixture: ComponentFixture<PerfilBarracaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PerfilBarracaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PerfilBarracaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
