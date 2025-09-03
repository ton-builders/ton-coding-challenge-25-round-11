const { Telegraf } = require('telegraf');
const { getAvailableGifts } = require('./getAvailableGifts');

const bot = new Telegraf(process.env.BOT_TOKEN);

bot.command('gifts', async (ctx) => {
  try {
    const gifts = await getAvailableGifts();
    if (!Array.isArray(gifts) || gifts.length === 0) {
      return ctx.reply('No gifts available');
    }

    const lines = gifts.map((gift, i) => {
      const emoji = gift.sticker?.emoji || '🎁';
      let msg = `${i + 1}. ${emoji} ${gift.star_count}⭐`;
      if (gift.remaining_count !== undefined && gift.total_count !== undefined) {
        msg += ' 可升级';
      }
      return msg;
    });

    ctx.reply(lines.join('\n'));
  } catch {
    ctx.reply('Error while getting gifts');
  }
});

bot.launch();

process.once('SIGINT', () => bot.stop());
process.once('SIGTERM', () => bot.stop());
