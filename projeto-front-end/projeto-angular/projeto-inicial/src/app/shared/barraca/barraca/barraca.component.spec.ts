import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BarracaComponent } from './barraca.component';

describe('BarracaComponent', () => {
  let component: BarracaComponent;
  let fixture: ComponentFixture<BarracaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BarracaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BarracaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
