import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Campaign-card.component.html',
  styleUrls: ['./Campaign-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Campaign-card]': 'true'
  }
})

export class CampaignCardComponent {


}