import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AppMenuSideComponent } from './app-menu-side.component';

describe('AppMenuSideComponent', () => {
  let component: AppMenuSideComponent;
  let fixture: ComponentFixture<AppMenuSideComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AppMenuSideComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AppMenuSideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
