import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Supply-card.component.html',
  styleUrls: ['./Supply-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Supply-card]': 'true'
  }
})

export class SupplyCardComponent {


}