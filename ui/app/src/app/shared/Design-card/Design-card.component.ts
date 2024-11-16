import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Design-card.component.html',
  styleUrls: ['./Design-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Design-card]': 'true'
  }
})

export class DesignCardComponent {


}