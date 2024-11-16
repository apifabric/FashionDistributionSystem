import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Collection-card.component.html',
  styleUrls: ['./Collection-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Collection-card]': 'true'
  }
})

export class CollectionCardComponent {


}