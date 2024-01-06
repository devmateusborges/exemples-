import { Component, OnInit, ViewChild } from '@angular/core';
import {ConfirmationService} from 'primeng/api';

@Component({
  selector: 'app-app-login',
  templateUrl: './app-login.component.html',
  styleUrls: ['./app-login.component.scss']
})
export class AppLoginComponent implements OnInit {

  @ViewChild('username', { static: true }) username: string = '';
  @ViewChild('password', { static: true }) password: string = '';


  constructor(private confirmationService: ConfirmationService) { }


  ngOnInit(): void {

  }



}
