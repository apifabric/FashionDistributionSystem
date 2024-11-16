import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Participation-card.component.html',
  styleUrls: ['./Participation-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Participation-card]': 'true'
  }
})

export class ParticipationCardComponent {


}