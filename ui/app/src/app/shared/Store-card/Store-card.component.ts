import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Store-card.component.html',
  styleUrls: ['./Store-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Store-card]': 'true'
  }
})

export class StoreCardComponent {


}